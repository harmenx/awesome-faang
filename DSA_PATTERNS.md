# DSA Patterns Cheat Sheet

> A curated guide to common Data Structures & Algorithm patterns for FAANG-level interviews.  
> Includes pattern description, key insights, example problem types, and checklist.

---

## Table of Contents

1. [Sliding Window](#sliding-window)
2. [Two Pointers](#two-pointers)
3. [Fast & Slow Pointers](#fast--slow-pointers)
4. [Binary Search / Divide & Conquer](#binary-search--divide--conquer)
5. [Depth-First Search (DFS)](#depth-first-search-dfs)
6. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
7. [Dynamic Programming (DP)](#dynamic-programming-dp)
8. [Backtracking](#backtracking)
9. [Greedy](#greedy)
10. [Graph Patterns](#graph-patterns)
11. [Heap / Priority Queue](#heap--priority-queue)
12. [Union-Find](#union-find)

---

## Sliding Window

**Idea:** Maintain a window (fixed or variable) over a sequence to reduce redundant computation.  

**Common Problems:**  
- Maximum sum subarray of size k  
- Longest substring with k distinct characters  
- Minimum window substring  

**Checklist:**  
- Decide window size (fixed or dynamic)  
- Track counts or sums inside the window  
- Move left pointer when conditions are violated  
- Update result after each right pointer increment  

**Example:**  
- [LeetCode 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Two Pointers

**Idea:** Use two indices to traverse array/list for sorted data or pair relationships.  

**Common Problems:**  
- Two sum in sorted array  
- Container with most water  
- Merge sorted arrays  

**Checklist:**  
- Ensure input is sorted (or sort it)  
- Initialize left and right pointers  
- Decide movement based on condition  
- Avoid duplicates if required  

**Example:**  
- [LeetCode 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## Fast & Slow Pointers (Cycle Detection)

**Idea:** Two pointers move at different speeds to detect cycles or middle elements.  

**Common Problems:**  
- Linked list cycle detection  
- Find middle of linked list  
- Happy number problem  

**Checklist:**  
- Initialize slow = head, fast = head  
- Move slow by 1, fast by 2  
- Check if pointers meet (cycle) or fast reaches end (no cycle)  

**Example:**  
- [LeetCode 142: Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

---

## Binary Search / Divide & Conquer

**Idea:** Repeatedly divide search space to reduce complexity.  

**Common Problems:**  
- Search in rotated sorted array  
- Median of two sorted arrays  
- Peak element  

**Checklist:**  
- Check sortedness or monotonicity  
- Define search space (indices, values)  
- Update left/right based on mid comparison  
- Watch for off-by-one errors  

**Example:**  
- [LeetCode 33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## Depth-First Search (DFS)

**Idea:** Explore as far as possible along a branch before backtracking.  

**Common Problems:**  
- Number of islands  
- Word search  
- Subsets / permutations  

**Checklist:**  
- Decide recursion vs stack-based iterative DFS  
- Mark visited nodes  
- Handle backtracking properly  
- Accumulate results along the path  

**Example:**  
- [LeetCode 200: Number of Islands](https://leetcode.com/problems/number-of-islands/)

---

## Breadth-First Search (BFS)

**Idea:** Explore neighbor nodes level by level.  

**Common Problems:**  
- Shortest path in unweighted graph  
- Level order traversal  
- Rotting oranges  

**Checklist:**  
- Use queue for BFS  
- Track visited nodes  
- Track levels if needed  
- Update result at correct point  

**Example:**  
- [LeetCode 127: Word Ladder](https://leetcode.com/problems/word-ladder/)

---

## Dynamic Programming (DP)

**Idea:** Break problem into overlapping subproblems and store results to avoid recomputation.  

**Common Problems:**  
- Fibonacci / climbing stairs  
- Longest increasing subsequence  
- Knapsack  

**Checklist:**  
- Identify subproblem  
- Decide memoization vs tabulation  
- Define state clearly (dp[i] or dp[i][j])  
- Handle base cases carefully  

**Example:**  
- [LeetCode 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## Backtracking

**Idea:** Explore all possibilities recursively and prune invalid paths.  

**Common Problems:**  
- N-Queens  
- Word search  
- Permutations / combinations  

**Checklist:**  
- Recursive helper with path state  
- Add/remove elements during recursion  
- Stop recursion when invalid  
- Accumulate results at leaves  

**Example:**  
- [LeetCode 51: N-Queens](https://leetcode.com/problems/n-queens/)

---

## Greedy

**Idea:** Make the locally optimal choice at each step.  

**Common Problems:**  
- Interval scheduling / meeting rooms  
- Minimum number of coins  
- Jump game  

**Checklist:**  
- Sort input if needed  
- Check if greedy choice leads to global optimum  
- Track state efficiently  

**Example:**  
- [LeetCode 435: Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

---

## Graph Patterns

**Idea:** Graph traversal & representation patterns.  

**Common Problems:**  
- Dijkstra / shortest path  
- Topological sort  
- Connected components  

**Checklist:**  
- Choose adjacency list vs matrix  
- Decide BFS, DFS, or priority queue  
- Track visited nodes  
- Detect cycles if needed  

**Example:**  
- [LeetCode 207: Course Schedule](https://leetcode.com/problems/course-schedule/)

---

## Heap / Priority Queue

**Idea:** Use a heap to efficiently track min/max elements.  

**Common Problems:**  
- Kth largest element  
- Merge k sorted lists  
- Top K frequent elements  

**Checklist:**  
- Use min-heap or max-heap as appropriate  
- Push/pop correctly  
- Heapify for bulk operations  

**Example:**  
- [LeetCode 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

---

## Union-Find (Disjoint Set)

**Idea:** Track connected components and efficiently merge sets.  

**Common Problems:**  
- Number of connected components  
- Redundant connections  
- Detect cycles in undirected graph  

**Checklist:**  
- Initialize parent array  
- Implement find with path compression  
- Implement union with rank optimization  

**Example:**  
- [LeetCode 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/)

---

## Tips for Using This Sheet

1. Solve **pattern-wise**, not random LeetCode problems.  
2. Memorize **checklists** per pattern.  
3. Time-box daily practice (1–2 patterns per day).  
4. Gradually mix patterns in **mock interviews**.  
5. Keep this sheet open as a **mental roadmap** during coding rounds.

---
