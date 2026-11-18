# Behavioral Interviews

Behavioral rounds decide more offers than candidates expect. At Amazon they carry as much weight as coding. Everywhere, they decide your level: the same technical performance can earn a senior or a mid-level offer depending on the scope of the stories you tell.

## Contents

- [What interviewers score](#what-interviewers-score)
- [Telling a story well](#telling-a-story-well)
- [Build a story bank](#build-a-story-bank)
- [A worked example](#a-worked-example)
- [Question bank](#question-bank)
- [Amazon Leadership Principles](#amazon-leadership-principles)
- [Scope by level](#scope-by-level)
- [Red flags](#red-flags)
- [Questions to ask them](#questions-to-ask-them)

## What interviewers score

Interviewers take notes against a rubric, then argue for or against you in a debrief. Give them evidence they can write down.

| Signal | What a strong answer shows |
| --- | --- |
| Ownership | You took responsibility without being asked and saw the work through. |
| Impact | The result mattered, and you can measure it. |
| Scope | The problem was as large as the level you are interviewing for. |
| Handling conflict | You disagreed directly and respectfully, used data, and kept the relationship. |
| Dealing with ambiguity | You made progress without a clear plan, and made reasonable assumptions. |
| Learning | You changed how you work after a mistake or feedback. |
| Collaboration | You made people around you more effective. |

Company emphasis differs. Amazon scores against its [Leadership Principles](#amazon-leadership-principles). Google looks for "Googleyness and leadership": working well in ambiguity, collaborating, and doing the right thing for users. Meta focuses on impact, conflict, and growth. Netflix tests fit with its [culture memo](https://jobs.netflix.com/culture).

## Telling a story well

Use the STAR structure, but spend your time where the score is.

| Part | Share of the answer | What to include |
| --- | --- | --- |
| **Situation** | 10% | One or two sentences of context. Skip the company history. |
| **Task** | 10% | Your specific responsibility, and why it was hard. |
| **Action** | 60% | What *you* did, step by step, and why you chose it over the alternatives. |
| **Result** | 20% | Measurable outcome, what you learned, what you would do differently. |

Rules that separate strong answers from average ones:

- **Say "I", not "we".** Interviewers cannot hire your team. Describe your own decisions, even on group work.
- **Use numbers.** "Cut p99 latency from 900 ms to 250 ms" beats "made it much faster".
- **Keep each story to about two to three minutes,** then stop. Follow-up questions are where interviewers dig for the signal, so leave room for them.
- **Show the trade-off.** Mention the option you rejected and why.
- **End with the lesson.** One sentence on what you would repeat or change.

## Build a story bank

Prepare six to eight stories that between them cover every row below. Most stories answer several questions, so you do not need one per question.

| Theme | Prepare a story about |
| --- | --- |
| Biggest impact | The project you are proudest of, with numbers |
| Failure | A mistake you caused, what you did about it, and what changed afterwards |
| Conflict | A real disagreement with a peer or manager, and how it was resolved |
| Ambiguity | Delivering something when the goal or the approach was unclear |
| Influence | Changing a decision you did not own |
| Tight deadline | Delivering under pressure, and what you cut or simplified |
| Helping others | Mentoring, unblocking, or improving the team's process |
| Customer focus | Going beyond the ask because of what users needed |

Write each story down as STAR bullet points. Practise saying it out loud; written stories always run long when spoken.

## A worked example

> **Tell me about a time you disagreed with your team.**
>
> **Situation.** Our checkout service was missing its latency target during sales, and the team planned to add a cache in front of the pricing service.
>
> **Task.** I owned checkout performance, and I thought the cache would hide the problem and risk showing stale prices.
>
> **Action.** I profiled a sale-day replay and found that 70% of the time was spent in three sequential calls to pricing, not in pricing itself. I wrote a one-page comparison of caching versus parallelizing the calls, covering latency, correctness risk, and effort, and shared it before the planning meeting rather than arguing in it. My tech lead preferred the cache because it was quicker to ship. We agreed to prototype both for two days. I built the parallel version and load-tested both.
>
> **Result.** Parallel calls cut p99 latency from 900 ms to 310 ms with no stale-price risk, and the team chose it. We shipped a week before the next sale, which ran without a latency alert. I learned to bring data to a disagreement early and to propose a cheap experiment instead of a debate.

Notice the "I" statements, the numbers, the alternative that was considered, and the respectful handling of the tech lead.

## Question bank

Common questions, grouped by what they are testing.

**Failure and learning**

- Tell me about your biggest mistake. *Tests:* ownership and how fast you learn. *Strong:* you caused it, caught it, fixed it, and changed a habit. *Weak:* blaming others, or a "failure" that is secretly a success.
- Tell me about a time you got critical feedback. *Tests:* self-awareness. *Strong:* you acted on it and can show the change.

**Conflict**

- Tell me about a disagreement with a teammate. *Tests:* emotional control and professionalism. *Strong:* direct conversation, data, a clear resolution. *Weak:* avoiding the conflict, or escalating straight to a manager.
- Describe a time you disagreed with your manager. *Tests:* backbone and commitment. *Strong:* you argued with evidence, then fully supported the final decision even when it went against you.

**Ambiguity and judgment**

- Tell me about a project with unclear requirements. *Tests:* comfort without a plan. *Strong:* you clarified what you could, made explicit assumptions, and adjusted as you learned.
- Tell me about a decision you made without enough data. *Tests:* judgment. *Strong:* you named the risk, chose a reversible step, and set a point to revisit.

**Impact and ownership**

- What is the most impactful thing you have built? *Tests:* scope and results. *Strong:* a measurable outcome and your specific part in it.
- Tell me about a time you went beyond your role. *Tests:* ownership. *Strong:* you saw a problem nobody owned and fixed it.

**Collaboration and leadership**

- Tell me about a time you helped a struggling teammate. *Tests:* empathy and team focus.
- Tell me about a time you influenced people who did not report to you. *Tests:* leadership without authority, which matters most at senior levels.

**Motivation**

- Why this company? Why this team? *Tests:* whether you did your homework. Mention something specific about their product or engineering.

## Amazon Leadership Principles

Amazon interviewers are each assigned a few principles to probe. Expect principle questions in most interviews, including the technical ones, and have at least one story for every principle.

| Principle | A question it often produces |
| --- | --- |
| Customer Obsession | Tell me about a time you went out of your way for a customer. |
| Ownership | Tell me about a time you took on something outside your responsibilities. |
| Invent and Simplify | Tell me about a time you found a simpler way to do something. |
| Are Right, A Lot | Tell me about a time you made a decision with incomplete data. |
| Learn and Be Curious | Tell me about something you learned recently that changed how you work. |
| Hire and Develop the Best | Tell me about a time you helped someone grow. |
| Insist on the Highest Standards | Tell me about a time you refused to compromise on quality. |
| Think Big | Tell me about a time you proposed a bold idea. |
| Bias for Action | Tell me about a time you acted quickly on a calculated risk. |
| Frugality | Tell me about a time you achieved more with fewer resources. |
| Earn Trust | Tell me about a time you admitted a mistake to your team. |
| Dive Deep | Tell me about a problem you solved by digging into the details. |
| Have Backbone; Disagree and Commit | Tell me about a time you disagreed with a decision and then committed to it. |
| Deliver Results | Tell me about a time you delivered despite serious obstacles. |
| Strive to be Earth's Best Employer | Tell me about a time you made your team a better place to work. |
| Success and Scale Bring Broad Responsibility | Tell me about a time you considered the wider impact of your work. |

One interviewer in each loop, the Bar Raiser, comes from outside the hiring team and can veto the hire. They often ask the hardest follow-ups. Read [the official principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) before your loop.

## Scope by level

| Level | Stories should show |
| --- | --- |
| New graduate and early career | Learning quickly, owning your tasks, working well with others. Internships, projects, and school work count. |
| Mid-level | Owning features end to end and handling conflict within your team. |
| Senior | Leading projects across teams, making technical decisions that others follow, mentoring. |
| Staff and above | Setting direction across an organization, influencing without authority, multi-quarter impact. |

If your stories are smaller than the level you are applying for, you may be offered the level below.

## Red flags

- Blaming teammates, managers, or "the company" for a failure.
- No measurable result, or results that belong to the team rather than you.
- Stories that contradict your resume.
- Speaking badly about a current or past employer.
- A rehearsed monologue that ignores the question that was asked.
- No questions for the interviewer at the end.

## Questions to ask them

Ask two or three questions that show you are evaluating them too.

- What does success look like for this role in the first six months?
- What is the hardest technical problem the team is working on now?
- How does the team decide what to build next?
- What do you enjoy most, and least, about working here?
- How are on-call and incidents handled?
