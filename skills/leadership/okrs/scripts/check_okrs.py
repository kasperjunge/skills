#!/usr/bin/env python3
"""Check the format of OKR documents (okrs-<yyyy>.md).

Usage: check_okrs.py FILE [FILE ...]

Prints errors and warnings as `path:line: level: message`.
Exits with 1 if any file has errors, 2 on wrong usage, otherwise 0.
The format is described in record/format.md.
"""

import re
import sys
from pathlib import Path

MAX_OBJECTIVES = 5  # per parent, and at the top level
MAX_KEY_RESULTS = 5  # per objective

ID = r"[1-9]\d*(?:\.[1-9]\d*)*"
FILENAME = re.compile(r"^okrs-(\d{4})\.md$")
TITLE = re.compile(r"^# OKRs (\d{4})$")
HEADING = re.compile(r"^ {0,3}#{1,6}(\s|$)")
OBJECTIVE = re.compile(rf"^## O({ID}): \S")
KEY_RESULT = re.compile(rf"^- KR({ID}): \S")
LIST_ITEM = re.compile(r"^([-*+]|\d+[.)])(\s|$)")
RULE = re.compile(r"^([-=*_])\1{2,}\s*$")
STATUS = re.compile(r"^Status: (draft|active|closed)$")
OWNER = re.compile(r"^Owner: \S")
RESULT = re.compile(r"^- Result: \S")
SCORE = re.compile(r"^- Score:\s*(.*)$")
SCORE_VALUE = re.compile(r"^(0(\.\d+)?|1(\.0+)?)$")
PLACEHOLDER = re.compile(r"(?<!\])\[[^\]\[]+\](?![(\[:])")


def fmt(id_):
    return ".".join(str(n) for n in id_)


def parse_id(text):
    return tuple(int(n) for n in text.split("."))


class Objective:
    def __init__(self, id_, line):
        self.id = id_
        self.line = line
        self.has_owner = False
        self.started = False  # a non-blank line has followed the heading
        self.has_description = False
        self.key_results = []  # KeyResult, in file order


class KeyResult:
    def __init__(self, id_, line):
        self.id = id_
        self.line = line
        self.has_result = False
        self.has_score = False


def check(path):
    """Return (errors, warnings) as lists of (line number, message)."""
    errors, warnings = [], []

    def error(line, message):
        errors.append((line, message))

    name = Path(path).name
    file_year = None
    match = FILENAME.match(name)
    if match:
        file_year = match.group(1)
    else:
        error(0, f"filename '{name}' must be okrs-<yyyy>.md, for example okrs-2027.md")

    try:
        text = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        error(0, f"cannot read file: {exc}")
        return errors, warnings

    lines = text.splitlines()

    # Title: the first non-blank line.
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index == len(lines):
        error(0, "file is empty; expected the title '# OKRs <yyyy>'")
        return errors, warnings
    match = TITLE.match(lines[index].rstrip())
    if not match:
        error(index + 1, "first line must be the title, exactly '# OKRs <yyyy>'")
    elif file_year and match.group(1) != file_year:
        error(index + 1, f"title year {match.group(1)} does not match filename year {file_year}")
    index += 1

    # Status: the next non-blank line.
    status = None
    while index < len(lines) and not lines[index].strip():
        index += 1
    match = STATUS.match(lines[index].rstrip()) if index < len(lines) else None
    if match:
        status = match.group(1)
        index += 1
    else:
        error(
            min(index + 1, len(lines)),
            "the line after the title must be 'Status: draft', 'Status: active', or 'Status: closed'",
        )

    for number, line in enumerate(lines, 1):
        for found in PLACEHOLDER.finditer(line):
            message = f"placeholder {found.group(0)} is not filled in"
            if status in ("active", "closed"):
                error(number, f"{message}; placeholders are only allowed when Status is draft")
            else:
                warnings.append((number, message))

    objectives = {}  # id -> Objective
    children = {}  # parent id -> list of child last numbers
    current = None
    in_key_results = False
    in_fence = False
    stray_reported = False

    def close(objective):
        if objective is None:
            return
        if not objective.has_owner:
            error(
                objective.line,
                f"O{fmt(objective.id)} has no owner; expected 'Owner: <name>' directly under the heading",
            )
        if not objective.has_description:
            error(objective.line, f"O{fmt(objective.id)} has no description")
        if status == "closed":
            for kr in objective.key_results:
                missing = [
                    name
                    for name, present in (("Result", kr.has_result), ("Score", kr.has_score))
                    if not present
                ]
                if missing:
                    error(
                        kr.line,
                        f"KR{fmt(kr.id)} has no {' and no '.join(missing)}; both are required when Status is closed",
                    )
        if not objective.key_results:
            error(objective.line, f"O{fmt(objective.id)} has no key results; expected 1 to {MAX_KEY_RESULTS}")
        elif len(objective.key_results) > MAX_KEY_RESULTS:
            error(
                objective.line,
                f"O{fmt(objective.id)} has {len(objective.key_results)} key results; the maximum is {MAX_KEY_RESULTS}",
            )

    for number, raw in enumerate(lines[index:], index + 1):
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith(("```", "~~~")):
            error(number, "code blocks are not allowed")
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if HEADING.match(line):
            match = OBJECTIVE.match(line)
            if not match:
                error(number, "heading must be an objective: '## O<id>: <title>', for example '## O1.2: Title'")
                continue
            close(current)
            id_ = parse_id(match.group(1))
            parent = id_[:-1]
            previous = current.id if current else ()
            if id_ in objectives:
                error(number, f"O{fmt(id_)} is already defined on line {objectives[id_].line}")
            elif parent and parent not in objectives:
                error(number, f"O{fmt(id_)} has no parent: O{fmt(parent)} is not defined above it")
            elif previous[: len(parent)] != parent:
                error(number, f"O{fmt(id_)} is out of order: it must come directly after O{fmt(parent)} and its sub-objectives")
            elif children.get(parent) and id_[-1] <= children[parent][-1]:
                error(number, f"O{fmt(id_)} is out of order: it comes after O{fmt(parent + (children[parent][-1],))}")
            children.setdefault(parent, []).append(id_[-1])
            current = Objective(id_, number)
            objectives.setdefault(id_, current)
            in_key_results = False
            stray_reported = False
            continue

        if current is None:
            if not stray_reported:
                error(number, "nothing but the status is allowed between the title and the first objective")
                stray_reported = True
            continue

        indented = line[0] in " \t"
        first_line = not current.started
        current.started = True
        if first_line and OWNER.match(line):
            current.has_owner = True
            continue

        if not indented and LIST_ITEM.match(line) and not RULE.match(line):
            match = KEY_RESULT.match(line)
            if not match:
                error(
                    number,
                    f"list item must be a key result: '- KR{fmt(current.id)}.<n>: <text>'",
                )
                in_key_results = True
                continue
            in_key_results = True
            id_ = parse_id(match.group(1))
            seen = [kr.id[-1] for kr in current.key_results]
            if id_[:-1] != current.id:
                error(number, f"KR{fmt(id_)} does not belong to O{fmt(current.id)}; expected KR{fmt(current.id)}.<n>")
            elif id_[-1] in seen:
                error(number, f"KR{fmt(id_)} is defined more than once")
            elif seen and id_[-1] < seen[-1]:
                error(number, f"KR{fmt(id_)} is out of order: it comes after KR{fmt(current.id + (seen[-1],))}")
            current.key_results.append(KeyResult(id_, number))
            continue

        if in_key_results:
            if not indented:
                error(number, "text after the key results is not allowed; indent lines that continue a key result")
            elif LIST_ITEM.match(stripped):
                kr = current.key_results[-1] if current.key_results else None
                is_result = bool(RESULT.match(stripped))
                score = SCORE.match(stripped)
                if kr is None or not (is_result or score):
                    error(number, "the only sub-bullets allowed under a key result are '- Result: <text>' and '- Score: <0.0 to 1.0>'")
                elif status in ("draft", "active"):
                    error(number, "Result and Score are only allowed when Status is closed")
                elif is_result:
                    if kr.has_result:
                        error(number, f"KR{fmt(kr.id)} has more than one Result")
                    elif kr.has_score:
                        error(number, "Result must come before Score")
                    kr.has_result = True
                else:
                    if kr.has_score:
                        error(number, f"KR{fmt(kr.id)} has more than one Score")
                    elif not SCORE_VALUE.match(score.group(1).strip()):
                        error(number, "Score must be a number from 0.0 to 1.0, for example 'Score: 0.7'")
                    kr.has_score = True
            continue

        # Description.
        if indented:
            error(number, "description lines must not be indented")
        elif RULE.match(line):
            error(number, "horizontal rules and underlined headings are not allowed")
        elif stripped.startswith("|"):
            error(number, "tables are not allowed in a description")
        elif stripped.startswith(">"):
            error(number, "quotes are not allowed in a description")
        current.has_description = True

    close(current)

    top_level = children.get((), [])
    if not top_level and not any("objective" in message for _, message in errors):
        error(0, f"no objectives found; expected 1 to {MAX_OBJECTIVES}")
    for parent, numbers in children.items():
        if len(numbers) > MAX_OBJECTIVES:
            if parent:
                error(
                    objectives[parent].line if parent in objectives else 0,
                    f"O{fmt(parent)} has {len(numbers)} sub-objectives; the maximum is {MAX_OBJECTIVES}",
                )
            else:
                error(0, f"{len(numbers)} top-level objectives; the maximum is {MAX_OBJECTIVES}")

    return sorted(errors), warnings


def main(argv):
    paths = argv[1:]
    if not paths or paths[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if paths else 2

    failed = False
    for path in paths:
        errors, warnings = check(path)
        for level, items in (("error", errors), ("warning", warnings)):
            for line, message in items:
                where = f"{path}:{line}" if line else path
                print(f"{where}: {level}: {message}")
        if errors:
            failed = True
        summary = "FAIL" if errors else "OK"
        print(f"{path}: {summary} ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
