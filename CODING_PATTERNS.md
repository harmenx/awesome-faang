# CODING PATTERNS (FAANG)

This file is a **pattern-recognition playbook** for FAANG coding interviews.

FAANG interviews are not about cleverness.  
They are about **recognizing the pattern fast and executing cleanly**.

---

## 1. How Coding Interviews Are Actually Passed

Failure modes:
- Not recognizing the pattern
- Over-engineering
- Getting stuck mid-solution
- Poor time/space reasoning

Winning strategy:
1. Identify the pattern in <30 seconds
2. State it out loud
3. Implement a clean template
4. Explain complexity
5. Test edge cases

---

## 2. Pattern Recognition Cheat Sheet

| Signal | Pattern |
|------|--------|
| Subarray / substring | Sliding Window |
| Sorted array | Two Pointers |
| Top K / Kth | Heap |
| Dependencies | Graph (Topological Sort) |
| Min/max so far | Greedy |
| Repeated work | Memoization / DP |
| Nearest greater/smaller | Monotonic Stack |
| Connectivity | Union-Find |
| Shortest path | BFS / Dijkstra |

---

## 3. Sliding Window

**When to use:**
- Contiguous subarrays
- Max/min/longest/shortest
- Fixed or variable window

**Template:**
- Expand right pointer
- Update state
- Shrink left when invalid

**Common traps:**
- Forgetting to shrink
- Incorrect window validity condition

**Examples:**
- Longest substring without repeats
- Minimum window substring

---

## 4. Two Pointers

**When to use:**
- Sorted arrays
- Palindrome checks
- Pair sums

**Variants:**
- Same direction
- Opposite direction
- Fast/slow

**Common traps:**
- Pointer movement logic wrong
- Infinite loops

---

## 5. Hashing / Frequency Map

**When to use:**
- Counting
- Matching
- Deduplication

**Tradeoff:**
- Time: O(1) average
- Space: O(n)

**Common traps:**
- Forgetting to decrement/remove
- Key collisions (conceptually)

---

## 6. Monotonic Stack

**When to use:**
- Next greater/smaller element
- Histogram problems
- Span problems

**Rule:**
- Stack maintains increasing or decreasing order

**Common traps:**
- Forgetting to pop
- Mishandling equal values

---

## 7. Heap (Priority Queue)

**When to use:**
- Top K
- Streaming data
- Scheduling

**Patterns:**
- Min-heap for largest K
- Max-heap for smallest K

**Common traps:**
- Wrong heap type
- Forgetting to pop after push

---

## 8. Binary Search (Beyond Arrays)

**When to use:**
- Sorted space
- Answer space monotonicity

**Template:**
- Define predicate
- Shrink search space

**Common traps:**
- Off-by-one
- Infinite loop

---

## 9. BFS / DFS

**When to use:**
- Trees
- Graph traversal
- Shortest path (unweighted)

**BFS:**
- Level-order
- Shortest path

**DFS:**
- Exploration
- Backtracking

**Common traps:**
- Missing visited set
- Stack overflow (DFS)

---

## 10. Backtracking

**When to use:**
- Permutations
- Combinations
- Constraint satisfaction

**Rules:**
- Choose
- Explore
- Un-choose

**Common traps:**
- Not copying state
- Exponential blow-up

---

## 11. Dynamic Programming

**When to use:**
- Overlapping subproblems
- Optimal substructure

**Steps:**
1. Define state
2. Define transition
3. Base case
4. Order of computation

**Common traps:**
- Wrong state definition
- Missing base case

---

## 12. Greedy

**When to use:**
- Local optimal leads to global optimal
- Scheduling problems

**Proof requirement:**
- Explain why greedy works

**Common traps:**
- Using greedy when DP is needed

---

## 13. Union-Find (Disjoint Set)

**When to use:**
- Connectivity
- Cycles
- Grouping

**Optimizations:**
- Path compression
- Union by rank

**Common traps:**
- Forgetting to initialize parents

---

## 14. Graph Topological Sort

**When to use:**
- Dependencies
- Ordering constraints

**Methods:**
- Kahn’s algorithm
- DFS-based

**Common traps:**
- Not detecting cycles

---

## 15. Time & Space Complexity Mapping

| Pattern | Time | Space |
|------|------|------|
| Sliding Window | O(n) | O(1)–O(n) |
| Two Pointers | O(n) | O(1) |
| Heap | O(n log k) | O(k) |
| BFS / DFS | O(V+E) | O(V) |
| DP | O(states × transitions) | O(states) |

---

## 16. Interview Execution Checklist

- Name the pattern early
- Write clean code
- Handle edge cases
- State complexity
- Walk through example

---

## Final Rule

If you are thinking about **code** before the **pattern**, you are already behind.

Pattern first. Code second.
