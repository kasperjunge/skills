---
name: plain-english-standard
description: Writing standard for simple, direct, jargon-free plain English — explain mechanisms directly, keep substance, cut buzzwords, hype, filler, flattery, and uncalibrated claims. Use when writing or reviewing summaries, design docs, specs, reports, PR descriptions, or messages, or when text reads as vague, inflated, or padded.
---

# Plain-English Standard

Write in simple, direct, jargon-free plain English. The reader should understand what is true, how it works, and what to do, on the first read.

Plain does not mean shallow. Cut the words that carry no information, not the information.

## Rules

- **Explain mechanisms directly.** Say what happens and how: "the cache stores each response for 5 minutes", not "the caching layer optimizes performance".
- **Keep the substance.** Don't summarize away numbers, conditions, trade-offs, or limits. A shorter text that drops a fact the reader needs is worse.
- **No buzzwords or jargon.** Replace words like *leverage*, *synergy*, *empower*, *holistic*, and *best-in-class* with what is actually meant. Use a technical term only when it is the precise term and the reader knows it, or define it once.
- **No ungrounded promotional adjectives.** Drop *seamless*, *robust*, *powerful*, *blazingly fast*, *cutting-edge*, and *world-class* unless a measurement backs them. Prefer the measurement: "handles 10,000 requests per second", not "highly scalable".
- **No decorative adverbs.** Drop *seamlessly*, *effortlessly*, *literally*, *drastically*, *obviously*, *simply*, *just*, *clearly*, and *essentially*.
- **No filler.** Cut phrases like "it is important to note that", "in order to", "at the end of the day", and "it goes without saying".
- **No synonym pairs.** "quick and rapid" and "clean and elegant" say one thing twice. Keep one word, or none.
- **No flattery or subjective judgments.** Don't call ideas, code, or decisions *great*, *brilliant*, *perfect*, *beautiful*, or *terrible*. State what is true about them and why it matters.
- **No reflexive apologies.** When corrected, state the corrected fact or reasoning instead of "I apologize".
- **Calibrate claims to evidence.** A claim about existing or tested behaviour must match what was actually checked. "Tested on macOS" beats "works everywhere".
- **Keep caveats only where they change a decision.** For each caveat or disclaimer, choose one action:
  - *Drop* it if no reader decision depends on it.
  - *Calibrate* it to the verified scope.
  - *Relocate* it to the step where the reader makes the choice.
  - *Keep* it if concrete evidence backs it.
- **Prefer short sentences, active voice, and common words.** Write "use", not "utilize". Write "the script deletes the file", not "the file is deleted".

## Examples

| Before | After |
|---|---|
| We leverage a robust, seamless caching layer to drastically improve performance. | Responses are cached for 5 minutes, which cut median page load from 800 ms to 120 ms. |
| It is important to note that the migration may potentially cause some issues. | The migration locks the `orders` table for about 2 minutes. Run it outside business hours. |
| Great question! Simply run the command and everything just works. | Run `make deploy`. It builds the image and restarts the service. |
| This fully eliminates all race conditions. | This removes the race between the writer and the cleanup job. Other writers are not covered. |

## Check

- Can a newcomer understand each sentence without asking what a word means?
- Does every adjective and adverb carry information, or is it backed by a number?
- Does every claim match the evidence behind it?
- Does every caveat change something the reader will decide or do?
- Was any number, condition, trade-off, or limit lost while shortening?
