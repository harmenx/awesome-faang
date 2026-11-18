# Study Plan

A plan you can follow from today to your onsite. Pick the track that matches your time, keep the order, and adjust the pace, not the sequence.

## Contents

- [Before you start](#before-you-start)
- [Eight-week plan](#eight-week-plan)
- [Four-week plan](#four-week-plan)
- [Twelve weeks or more](#twelve-weeks-or-more)
- [A study session](#a-study-session)
- [Tracking progress](#tracking-progress)
- [When are you ready?](#when-are-you-ready)

## Before you start

- **Pick one language** and stay with it. See [choosing a language](fundamentals.md#choosing-a-language).
- **Pick one problem list.** [Grind 75](https://www.techinterviewhandbook.org/grind75) or the [NeetCode roadmap](https://neetcode.io/roadmap) both work. Finishing one beats starting three.
- **Book a mock interview for week four now.** A date on the calendar keeps the plan honest.
- **Plan about 10 to 15 hours a week** for the eight-week track. More helps; less than that, use the twelve-week track.

## Eight-week plan

Each week assumes about five practice days. Patterns link to [coding patterns](coding-patterns.md).

| Week | Coding | Design and behavioral |
| --- | --- | --- |
| 1 | Hash maps, two pointers, sliding window. Review [fundamentals](fundamentals.md). | List your projects and draft three stories for the [story bank](behavioral.md#build-a-story-bank). |
| 2 | Prefix sums, binary search, linked lists, stacks | Draft the remaining stories. |
| 3 | Trees: depth-first and breadth-first search, binary search trees | Read the [45-minute plan](system-design.md#a-45-minute-plan) and the building blocks. |
| 4 | Heaps, intervals, greedy. **First mock coding interview.** | One design problem a week from now on, timed, out loud: start with a URL shortener. |
| 5 | Graphs: islands, BFS on grids, topological sort, union-find | Design: rate limiter. Practise telling two stories out loud. |
| 6 | Backtracking and dynamic programming, 1D | Design: news feed. **First mock design interview.** |
| 7 | Dynamic programming, 2D; tries; Dijkstra's algorithm | Design: chat. Read the [company guide](companies.md) for each target. |
| 8 | Mixed problems at random, timed at 25 to 35 minutes each. Redo problems you failed. | Two more mocks: one coding, one design. Rehearse every story once. |

New graduates without a design round should use the design time for extra coding practice and a second pass through behavioral stories.

## Four-week plan

For a loop that is already scheduled. Cover breadth first, then sharpen.

| Week | Focus |
| --- | --- |
| 1 | Hash maps, two pointers, sliding window, binary search, trees. Draft your story bank. |
| 2 | Heaps, intervals, graphs, topological sort. Learn the design framework and do one design problem. |
| 3 | Backtracking, dynamic programming. Two mock interviews. Two more design problems. |
| 4 | Mixed timed problems, company-tagged problems, story rehearsal, rest the day before. |

If you are short on time, cut the hardest dynamic programming and graph problems first. Medium problems in common patterns are most of what you will see.

## Twelve weeks or more

Follow the eight-week plan at a slower pace, and add:

- A pass through [Data Structures and Algorithms](../README.md#data-structures-and-algorithms) resources before week one if you are rusty or self-taught.
- A weekly contest on LeetCode or Codeforces from week six, to build speed under pressure.
- Two design problems a week in the second half, and a full read of *Designing Data-Intensive Applications* for senior roles.

## A study session

A focused 90-minute session beats a distracted four-hour one.

1. **Warm up, 10 minutes.** Redo one problem you solved last week, from memory.
2. **New problems, 60 minutes.** Two problems from today's pattern. Give each 25 to 30 minutes before reading a solution. Talk out loud as if an interviewer were there.
3. **Review, 20 minutes.** For each problem, write one line: the pattern, the key insight, and the mistake you made. These notes are what you will revise in the last week.

When you read a solution, close it and write the code yourself the next day. Recognizing a solution is not the same as producing one.

## Tracking progress

Keep a simple spreadsheet with one row per problem:

| Problem | Pattern | Date | Solved alone? | Time | Mistake | Redo on |
| --- | --- | --- | --- | --- | --- | --- |
| Number of Islands | Graph traversal | 3 Mar | No | 40 min | Forgot to mark visited when queuing | 10 Mar |

Revisit every "No" a week later. The redo list, not the total count, measures progress.

## When are you ready?

You are ready for coding rounds when you can:

- solve most unseen medium problems in common patterns in about 25 minutes, explaining as you go;
- state the time and space complexity without hesitating;
- test your own code with a small example and catch your bugs before the interviewer does.

You are ready for design rounds when you can complete the [45-minute plan](system-design.md#a-45-minute-plan) on a new problem and still have 15 minutes for deep dives.

You are ready for behavioral rounds when you have a story for every row of the [story bank](behavioral.md#build-a-story-bank) and can tell each in about two to three minutes.
