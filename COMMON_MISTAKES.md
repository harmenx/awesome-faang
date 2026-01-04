# COMMON MISTAKES (FAANG INTERVIEWS)

This file documents the **highest-frequency failure modes** in FAANG interviews.
Most candidates fail for predictable reasons. Avoid these and your odds increase materially.

---

## 1. Interview-Wide Mistakes

### 1.1 Not Clarifying the Problem
**Mistake:**
- Start coding immediately
- Assume constraints

**Why it fails:**
- Shows poor judgment
- Leads to wrong solution

**Fix:**
- Clarify inputs, outputs, constraints
- Restate the problem in your own words

---

### 1.2 Silent Problem Solving
**Mistake:**
- Thinking quietly
- Only talking after coding

**Why it fails:**
- Interviewer can’t evaluate reasoning
- Appears stuck or slow

**Fix:**
- Verbalize assumptions and decisions
- Think out loud clearly and concisely

---

### 1.3 Over-Engineering
**Mistake:**
- Complex abstractions
- Premature optimization

**Why it fails:**
- Wastes time
- Signals poor prioritization

**Fix:**
- Start with the simplest correct solution
- Optimize only if required

---

## 2. Coding-Specific Mistakes

### 2.1 Not Recognizing the Pattern
**Mistake:**
- Treat every problem as unique

**Why it fails:**
- Slow progress
- Bug-prone solutions

**Fix:**
- Map problem → known pattern within 30 seconds

---

### 2.2 Off-by-One Errors
**Mistake:**
- Incorrect loop bounds
- Index mismanagement

**Why it fails:**
- Basic correctness failure

**Fix:**
- State invariants
- Walk through a small example

---

### 2.3 Ignoring Edge Cases
**Mistake:**
- No handling for empty input
- No null checks

**Why it fails:**
- Production-unready mindset

**Fix:**
- Call out edge cases explicitly before coding

---

### 2.4 Poor Complexity Analysis
**Mistake:**
- Wrong Big-O
- No space analysis

**Why it fails:**
- Weak fundamentals signal

**Fix:**
- Always state time and space complexity
- Explain tradeoffs

---

### 2.5 Debugging in Silence
**Mistake:**
- Quietly scanning code

**Why it fails:**
- Looks like flailing

**Fix:**
- Explain what you’re checking and why

---

## 3. System Design Mistakes

### 3.1 Jumping to Architecture
**Mistake:**
- Drawing boxes immediately

**Why it fails:**
- Misses requirements
- Poor scope control

**Fix:**
- Clarify functional + non-functional requirements first

---

### 3.2 Ignoring Scale
**Mistake:**
- No numbers
- Vague scale assumptions

**Why it fails:**
- Unrealistic designs

**Fix:**
- Ask for QPS, data size, latency targets

---

### 3.3 No Failure Handling
**Mistake:**
- Happy-path only

**Why it fails:**
- Low production maturity signal

**Fix:**
- Discuss retries, timeouts, degradation

---

### 3.4 Overusing Buzzwords
**Mistake:**
- “Just use Kafka / Redis / Kubernetes”

**Why it fails:**
- Shallow understanding

**Fix:**
- Explain *why* each component exists

---

## 4. Behavioral Interview Mistakes

### 4.1 No Ownership
**Mistake:**
- “We did X”

**Why it fails:**
- Low accountability signal

**Fix:**
- Use “I” when describing actions

---

### 4.2 Blaming Others
**Mistake:**
- Throwing teammates or managers under the bus

**Why it fails:**
- High-risk hire signal

**Fix:**
- Take responsibility, explain mitigation

---

### 4.3 Vague Stories
**Mistake:**
- No metrics
- No outcome

**Why it fails:**
- Low credibility

**Fix:**
- Quantify impact
- Close the loop

---

### 4.4 Rambling
**Mistake:**
- Long, unfocused answers

**Why it fails:**
- Poor communication signal

**Fix:**
- Use STAR
- Keep answers under 2 minutes

---

## 5. Meta Mistakes

### 5.1 Not Knowing When You’re Wrong
**Mistake:**
- Defending broken logic

**Why it fails:**
- Low coachability

**Fix:**
- Acknowledge mistakes quickly
- Correct decisively

---

### 5.2 Freezing Under Pressure
**Mistake:**
- Mental shutdown after an error

**Why it fails:**
- Stress fragility signal

**Fix:**
- Pause, reset, reframe

---

### 5.3 Inconsistent Resume vs Interview
**Mistake:**
- Can’t explain listed experience

**Why it fails:**
- Trust failure

**Fix:**
- Be prepared to deep-dive any resume line

---

## 6. Final Rule

Most candidates fail **not because they are weak**, but because they make **predictable mistakes**.

Your goal is not to be perfect.

Your goal is to be:
- Clear
- Calm
- Correct enough
- Easy to hire

Avoid these mistakes and your success probability increases sharply.
