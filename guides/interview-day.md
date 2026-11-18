# Interview Day

How to run a coding round minute by minute, the mistakes that most often cost offers, and a checklist for the day itself.

## Contents

- [A 45-minute coding round](#a-45-minute-coding-round)
- [What to say when you are stuck](#what-to-say-when-you-are-stuck)
- [Common mistakes](#common-mistakes)
- [Virtual and in-person rounds](#virtual-and-in-person-rounds)
- [Checklist](#checklist)
- [After the interview](#after-the-interview)

## A 45-minute coding round

| Minutes | Step | What to do |
| --- | --- | --- |
| 0–3 | Introductions | Keep it to a sentence or two. The clock is running. |
| 3–8 | **Clarify** | Restate the problem. Ask about input size, empty input, duplicates, negative numbers, and the expected output format. Walk through the example. |
| 8–15 | **Plan** | State a brute-force approach and its complexity, then a better one. Agree on the approach before writing code. |
| 15–32 | **Code** | Write clean code with clear names. Narrate what you are doing. Use helper functions instead of one long block. |
| 32–40 | **Test** | Trace a small example line by line. Then try edge cases: empty input, one element, duplicates, the largest input. |
| 40–45 | **Wrap up** | State the final time and space complexity, mention possible improvements, and ask your questions. |

At companies that often ask two problems per round, compress each step and move on promptly.

## What to say when you are stuck

Silence is the worst signal you can give. Interviewers can only score what you say.

- "Let me try the brute force first, then look for repeated work."
- "Let me try a smaller example by hand to see the pattern."
- "If the input were sorted, I could use binary search. Is sorting allowed here?"
- "I am deciding between a heap and sorting. A heap is O(n log k), which is better if k is small."

Hints are normal and do not fail you on their own. Take them gracefully, use them, and keep going.

## Common mistakes

**Throughout the interview**

- Starting to code before clarifying the problem.
- Solving in silence, then explaining at the end.
- Over-engineering a simple problem.
- Not knowing when you are wrong, and defending a broken approach after the interviewer points at the flaw.

**In coding rounds**

- Off-by-one errors in loops, windows, and binary search. Check boundaries out loud.
- Ignoring edge cases until the interviewer asks.
- Stating the wrong complexity, or none at all.
- Debugging by random changes instead of tracing the code with an example.
- Missing the pattern. See the [recognition table](coding-patterns.md#recognition-table).

**In design rounds**

- Drawing architecture before agreeing on requirements.
- Ignoring scale, or estimating numbers that never change a decision.
- No plan for failures: what happens when this database or service goes down?
- Naming technologies without saying why. More in [system design](system-design.md#mistakes-that-cost-offers).

**In behavioral rounds**

- Saying "we" throughout, so the interviewer cannot tell what you did.
- Vague stories without results or numbers.
- Blaming others, or rambling past three minutes. More in [behavioral](behavioral.md#red-flags).

## Virtual and in-person rounds

**Virtual**

- Test your camera, microphone, and the interview platform the day before. Have a phone ready as a backup.
- Use a plain editor setup similar to the interview's, without autocomplete you rely on.
- Close other applications and turn off notifications.
- Only use tools the interviewer has explicitly allowed. Unapproved AI assistance is treated as cheating, and companies increasingly check for it.

**In person**

- Practise on a whiteboard or on paper. Writing code by hand is slower than typing, so leave space and write neatly.
- Bring water, and confirm the address, building, and arrival time with your recruiter.

## Checklist

**The week before**

- [ ] Confirm the rounds, their format, and the language options with your recruiter.
- [ ] Re-read your notes of mistakes from practice.
- [ ] Rehearse every story in your bank out loud once.
- [ ] Read the [company guide](companies.md) and something recent about the product or team.

**The day before**

- [ ] Do two or three easy or medium problems to warm up, nothing new or hard.
- [ ] Prepare questions for each interviewer.
- [ ] Sleep. A tired brain makes off-by-one errors.

**On the day**

- [ ] Eat beforehand, and have water nearby.
- [ ] Join or arrive ten minutes early.
- [ ] After a round goes badly, reset. Each interviewer scores independently, and many offers include one weak round.

## After the interview

- Write down every question you were asked while you still remember them. They are the best practice material for your next loop.
- Send a short thank-you to your recruiter if you like. It will not change the outcome, but it keeps the relationship good.
- If you are rejected, ask when you can reapply. Waiting periods of six to twelve months are common, and many engineers pass on a later attempt.
