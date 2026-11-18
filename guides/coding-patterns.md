# Coding Patterns

Most coding interview questions are a known pattern in disguise. Interviewers are not looking for a clever trick. They want to see you recognize the shape of the problem, pick an approach out loud, write it cleanly, and test it.

Each pattern below has the signals that point to it, a short Python template, its cost, the mistakes that sink candidates, and practice problems ordered from easier to harder. Every template runs and is tested in this repository's CI, so you can copy it with confidence.

## Contents

- [How to use this page](#how-to-use-this-page)
- [Recognition table](#recognition-table)
- [Hash map lookups](#hash-map-lookups)
- [Two pointers](#two-pointers)
- [Sliding window](#sliding-window)
- [Prefix sums](#prefix-sums)
- [Binary search](#binary-search)
- [Linked lists and fast and slow pointers](#linked-lists-and-fast-and-slow-pointers)
- [Monotonic stack](#monotonic-stack)
- [Heap and top K](#heap-and-top-k)
- [Intervals](#intervals)
- [Tree depth-first search](#tree-depth-first-search)
- [Breadth-first search](#breadth-first-search)
- [Graph traversal](#graph-traversal)
- [Topological sort](#topological-sort)
- [Union-find](#union-find)
- [Shortest paths with weights](#shortest-paths-with-weights)
- [Backtracking](#backtracking)
- [Dynamic programming](#dynamic-programming)
- [Trie](#trie)
- [Greedy](#greedy)
- [Bit manipulation](#bit-manipulation)

## How to use this page

1. Learn one pattern at a time. Read the template, then solve the first practice problem without looking.
2. When you get stuck for more than 25 minutes, read a solution, close it, and write it again from memory the next day.
3. Once you have done every pattern, mix problems at random. Recognizing the pattern without the section heading is the real skill.
4. Say your approach and its complexity before you write code. Interviewers score the reasoning, not just the result.

## Recognition table

| If the problem says or implies | Reach for |
| --- | --- |
| "Have I seen this before?", pairs that sum to a target, counting | [Hash map lookups](#hash-map-lookups) |
| Sorted array, pair or triplet with a target, palindrome | [Two pointers](#two-pointers) |
| Longest or shortest contiguous subarray or substring with a property | [Sliding window](#sliding-window) |
| Sum of a range, subarray sum equals K | [Prefix sums](#prefix-sums) |
| Sorted input, or "minimum value that still works" | [Binary search](#binary-search) |
| Cycle in a linked list, middle of a list | [Fast and slow pointers](#linked-lists-and-fast-and-slow-pointers) |
| Next greater or smaller element, spans, histograms | [Monotonic stack](#monotonic-stack) |
| K largest, K most frequent, running median, merge K sorted | [Heap and top K](#heap-and-top-k) |
| Overlapping ranges, meetings, merging | [Intervals](#intervals) |
| Anything on a binary tree | [Tree depth-first search](#tree-depth-first-search) |
| Fewest steps, level by level, nearest | [Breadth-first search](#breadth-first-search) |
| Grid of cells, islands, connected regions | [Graph traversal](#graph-traversal) |
| Prerequisites, build order, dependencies | [Topological sort](#topological-sort) |
| Merging groups, "are these connected", redundant edge | [Union-find](#union-find) |
| Cheapest or fastest route with weighted edges | [Shortest paths with weights](#shortest-paths-with-weights) |
| All subsets, permutations, combinations, placements | [Backtracking](#backtracking) |
| Count the ways, minimum cost, overlapping subproblems | [Dynamic programming](#dynamic-programming) |
| Prefix matching, autocomplete, many words at once | [Trie](#trie) |
| A locally best choice is provably globally best | [Greedy](#greedy) |
| Single number among pairs, powers of two, flags | [Bit manipulation](#bit-manipulation) |

## Hash map lookups

**Signals:** you need to know whether you have seen a value, how often, or where. A nested loop that searches for a partner is the brute force this replaces.

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([1, 2], 7) == []
```

**Cost:** O(n) time, O(n) space.

**Mistakes:** inserting the current value before checking, which pairs an element with itself; using a list where a set or dictionary gives constant-time lookups.

**Practice:** [1. Two Sum](https://leetcode.com/problems/two-sum/), [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/), [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/), [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Two pointers

**Signals:** sorted input, a pair or triplet with a target sum, or comparing the two ends of a sequence.

```python
def pair_with_sum(sorted_nums, target):
    left, right = 0, len(sorted_nums) - 1
    while left < right:
        total = sorted_nums[left] + sorted_nums[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def is_palindrome(text):
    chars = [c.lower() for c in text if c.isalnum()]
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left, right = left + 1, right - 1
    return True


assert pair_with_sum([1, 3, 4, 6, 9], 10) == (0, 4)
assert pair_with_sum([1, 2, 3], 100) is None
assert is_palindrome("A man, a plan, a canal: Panama")
assert not is_palindrome("race a car")
```

**Cost:** O(n) time after sorting, O(1) extra space.

**Mistakes:** forgetting to skip duplicates in 3Sum-style problems; using `<=` in the loop condition and pairing an element with itself.

**Practice:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/), [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), [15. 3Sum](https://leetcode.com/problems/3sum/), [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/), [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## Sliding window

**Signals:** "longest", "shortest", or "maximum" contiguous subarray or substring that satisfies a condition.

```python
from collections import defaultdict


def longest_without_repeats(s):
    last_seen = {}
    start = best = 0
    for end, char in enumerate(s):
        if last_seen.get(char, -1) >= start:
            start = last_seen[char] + 1
        last_seen[char] = end
        best = max(best, end - start + 1)
    return best


def longest_with_at_most_k_distinct(s, k):
    counts = defaultdict(int)
    start = best = 0
    for end, char in enumerate(s):
        counts[char] += 1
        while len(counts) > k:  # shrink until the window is valid again
            counts[s[start]] -= 1
            if counts[s[start]] == 0:
                del counts[s[start]]
            start += 1
        best = max(best, end - start + 1)
    return best


assert longest_without_repeats("abcabcbb") == 3
assert longest_without_repeats("bbbbb") == 1
assert longest_without_repeats("") == 0
assert longest_with_at_most_k_distinct("eceba", 2) == 3
assert longest_with_at_most_k_distinct("aa", 1) == 2
```

**Cost:** O(n) time, because each index enters and leaves the window once. Space is the size of the alphabet or the counts.

**Mistakes:** recomputing the whole window on every step; updating the answer before the window is valid again; leaving zero counts in the dictionary so its size is wrong.

**Practice:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/), [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/), [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/), [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

## Prefix sums

**Signals:** repeated range-sum queries, or "number of subarrays whose sum is K", especially when values can be negative and a sliding window no longer works.

```python
def count_subarrays_with_sum(nums, k):
    counts = {0: 1}  # prefix sum -> how many times seen
    running = total = 0
    for num in nums:
        running += num
        total += counts.get(running - k, 0)
        counts[running] = counts.get(running, 0) + 1
    return total


def range_sums(nums, queries):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return [prefix[right + 1] - prefix[left] for left, right in queries]


assert count_subarrays_with_sum([1, 1, 1], 2) == 2
assert count_subarrays_with_sum([1, -1, 0], 0) == 3
assert range_sums([-2, 0, 3, -5, 2, -1], [(0, 2), (2, 5), (0, 5)]) == [1, -1, -3]
```

**Cost:** O(n) to build, O(1) per range query.

**Mistakes:** forgetting the starting `{0: 1}`, which misses subarrays that begin at index 0; off-by-one errors between prefix indexes and array indexes.

**Practice:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

## Binary search

**Signals:** sorted input, a rotated sorted array, or a question of the form "the smallest X such that a condition holds" where the condition flips once from false to true. The last case is called binary search on the answer.

```python
def first_true(low, high, condition):
    """Smallest value in [low, high] where condition is true, or high + 1 if none."""
    while low <= high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low


def search(nums, target):
    index = first_true(0, len(nums) - 1, lambda i: nums[i] >= target)
    return index if index < len(nums) and nums[index] == target else -1


def min_eating_speed(piles, hours):
    def finishes(speed):
        return sum((pile + speed - 1) // speed for pile in piles) <= hours

    return first_true(1, max(piles), finishes)


assert search([-1, 0, 3, 5, 9, 12], 9) == 4
assert search([-1, 0, 3, 5, 9, 12], 2) == -1
assert min_eating_speed([3, 6, 7, 11], 8) == 4
assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
```

**Cost:** O(log n) searches, times the cost of checking the condition.

**Mistakes:** infinite loops from `low = mid` with `low < high`; checking the wrong half in rotated arrays. Using one template, such as `first_true` above, for every variant removes most of these bugs.

**Practice:** [704. Binary Search](https://leetcode.com/problems/binary-search/), [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/), [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/), [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/), [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Linked lists and fast and slow pointers

**Signals:** a linked list with a cycle, finding the middle, or the K-th node from the end. Most list problems also need a dummy head node to avoid special cases.

```python
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def build(values):
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def reverse(head):
    previous = None
    while head:
        head.next, previous, head = previous, head, head.next
    return previous


def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


assert to_list(reverse(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
assert reverse(None) is None
assert middle(build([1, 2, 3, 4, 5])).val == 3
looped = build([3, 2, 0, -4])
looped.next.next.next.next = looped.next
assert has_cycle(looped)
assert not has_cycle(build([1, 2]))
```

**Cost:** O(n) time, O(1) space.

**Mistakes:** losing the rest of the list by overwriting `next` before saving it; not handling an empty list or a single node.

**Practice:** [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/), [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/), [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/), [143. Reorder List](https://leetcode.com/problems/reorder-list/), [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/), [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

## Monotonic stack

**Signals:** "next greater element", "days until a warmer temperature", spans, or the largest rectangle in a histogram. Keep a stack whose values only increase or only decrease, and resolve waiting items when a new value breaks the order.

```python
def days_until_warmer(temperatures):
    answer = [0] * len(temperatures)
    waiting = []  # indexes with no warmer day yet, temperatures decreasing
    for day, temperature in enumerate(temperatures):
        while waiting and temperatures[waiting[-1]] < temperature:
            earlier = waiting.pop()
            answer[earlier] = day - earlier
        waiting.append(day)
    return answer


def largest_rectangle(heights):
    best = 0
    stack = []  # (start index, height), heights increasing
    for i, height in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] >= height:
            start, tall = stack.pop()
            best = max(best, tall * (i - start))
        stack.append((start, height))
    return best


assert days_until_warmer([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle([2, 4]) == 4
```

**Cost:** O(n), because each index is pushed and popped once.

**Mistakes:** storing values when you need indexes to compute distances; forgetting to flush the stack at the end, which the trailing `0` above handles.

**Practice:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/), [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/), [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/), [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Heap and top K

**Signals:** the K largest, smallest, closest, or most frequent items, merging K sorted lists, or a running median.

```python
import heapq
from collections import Counter


def k_largest(nums, k):
    heap = []  # min-heap of the k largest seen so far
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)


def top_k_frequent(nums, k):
    return [value for value, _ in Counter(nums).most_common(k)]


def merge_sorted(lists):
    heap = [(values[0], i, 0) for i, values in enumerate(lists) if values]
    heapq.heapify(heap)
    merged = []
    while heap:
        value, which, index = heapq.heappop(heap)
        merged.append(value)
        if index + 1 < len(lists[which]):
            heapq.heappush(heap, (lists[which][index + 1], which, index + 1))
    return merged


class RunningMedian:
    def __init__(self):
        self.low = []   # max-heap, stored negated
        self.high = []  # min-heap

    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2


assert k_largest([3, 2, 1, 5, 6, 4], 2) == [6, 5]
assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
assert merge_sorted([[1, 4, 5], [1, 3, 4], [2, 6], []]) == [1, 1, 2, 3, 4, 4, 5, 6]
stream = RunningMedian()
for value, expected in [(1, 1), (2, 1.5), (3, 2), (10, 2.5)]:
    stream.add(value)
    assert stream.median() == expected
```

**Cost:** O(n log k) for top K, O(N log k) to merge K lists with N items in total.

**Mistakes:** using a max-heap for the K largest, which costs O(n log n); forgetting that Python's `heapq` is a min-heap only, so a max-heap needs negated values; comparing objects that are not orderable, which the index in each tuple above avoids.

**Practice:** [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/), [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/), [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/), [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/), [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/), [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

## Intervals

**Signals:** meetings, bookings, ranges that may overlap. Almost every interval problem starts by sorting, by start time or by end time.

```python
def merge(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def min_removals_to_avoid_overlap(intervals):
    removed = 0
    previous_end = float("-inf")
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        if start >= previous_end:
            previous_end = end  # keep the interval that ends earliest
        else:
            removed += 1
    return removed


assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
assert min_removals_to_avoid_overlap([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
```

**Cost:** O(n log n) for the sort, O(n) for the sweep.

**Mistakes:** sorting by start when the greedy choice needs the earliest end; treating touching intervals as overlapping, or not, without asking which the problem wants.

**Practice:** [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/), [57. Insert Interval](https://leetcode.com/problems/insert-interval/), [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/), [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/), [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

## Tree depth-first search

**Signals:** any binary tree question. Decide what each call returns to its parent, then write the base case for an empty node.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if not node:
        return True
    if not low < node.val < high:
        return False
    return is_valid_bst(node.left, low, node.val) and is_valid_bst(node.right, node.val, high)


def max_path_sum(root):
    best = float("-inf")

    def gain(node):  # best downward path starting at node
        nonlocal best
        if not node:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)  # path that bends here
        return node.val + max(left, right)

    gain(root)
    return best


tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert max_depth(tree) == 3
assert max_path_sum(tree) == 42
assert is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3)))
assert not is_valid_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
```

**Cost:** O(n) time, O(h) stack space where h is the tree height.

**Mistakes:** checking a BST only against the parent instead of the whole valid range; mixing up what a function returns with the global answer it updates, as in path-sum problems.

**Practice:** [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/), [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/), [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/), [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/), [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/), [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/), [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/), [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Breadth-first search

**Signals:** the fewest steps or moves, level-by-level output, or the nearest of something in an unweighted graph or grid.

```python
from collections import deque


def level_order(root):
    if not root:
        return []
    levels, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # exactly one level per pass
            node = queue.popleft()
            level.append(node.val)
            queue.extend(child for child in (node.left, node.right) if child)
        levels.append(level)
    return levels


def shortest_path_in_grid(grid):
    """Fewest moves from top-left to bottom-right through 0 cells, or -1."""
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] or grid[rows - 1][cols - 1]:
        return -1
    queue = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == (rows - 1, cols - 1):
            return steps
        for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            r, c = row + d_row, col + d_col
            if 0 <= r < rows and 0 <= c < cols and not grid[r][c] and (r, c) not in seen:
                seen.add((r, c))  # mark when queued, not when popped
                queue.append((r, c, steps + 1))
    return -1


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


assert level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3], [9, 20], [15, 7]]
assert shortest_path_in_grid([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 4
assert shortest_path_in_grid([[0, 1], [1, 0]]) == -1
```

**Cost:** O(V + E) for graphs, O(rows × cols) for grids.

**Mistakes:** marking cells visited when they are popped instead of when they are queued, which adds duplicates; using depth-first search for a shortest path; using a list's `pop(0)`, which is O(n), instead of `deque.popleft()`.

**Practice:** [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/), [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/), [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/), [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

## Graph traversal

**Signals:** islands, regions, connected components, copying a graph, or anything on a grid where cells connect to neighbors.

```python
def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()

    def flood(row, col):
        stack = [(row, col)]  # iterative, so deep grids cannot overflow the call stack
        seen.add((row, col))
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))

    islands = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in seen:
                flood(row, col)
                islands += 1
    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
assert count_islands(grid) == 3
assert count_islands([["0"]]) == 0
```

**Cost:** O(V + E), or O(rows × cols) for a grid.

**Mistakes:** recursion depth errors on large grids in Python, avoided above with an explicit stack; changing the input grid without asking whether that is allowed.

**Practice:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/), [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/), [133. Clone Graph](https://leetcode.com/problems/clone-graph/), [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/), [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/), [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Topological sort

**Signals:** prerequisites, build order, task dependencies, or detecting a cycle in a directed graph.

```python
from collections import deque


def course_order(count, prerequisites):
    """Kahn's algorithm. Returns an order, or [] if a cycle makes it impossible."""
    graph = [[] for _ in range(count)]
    indegree = [0] * count
    for course, required in prerequisites:
        graph[required].append(course)
        indegree[course] += 1
    ready = deque(course for course in range(count) if indegree[course] == 0)
    order = []
    while ready:
        course = ready.popleft()
        order.append(course)
        for unlocked in graph[course]:
            indegree[unlocked] -= 1
            if indegree[unlocked] == 0:
                ready.append(unlocked)
    return order if len(order) == count else []


assert course_order(2, [[1, 0]]) == [0, 1]
assert course_order(2, [[1, 0], [0, 1]]) == []
order = course_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
assert order.index(0) < order.index(1) < order.index(3) and order.index(2) < order.index(3)
```

**Cost:** O(V + E).

**Mistakes:** reversing the edge direction; forgetting that a result shorter than the number of nodes means there is a cycle.

**Practice:** [207. Course Schedule](https://leetcode.com/problems/course-schedule/), [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/), [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (premium)

## Union-find

**Signals:** grouping items as connections arrive, "are A and B connected", finding a redundant edge, or Kruskal's minimum spanning tree.

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.groups = size

    def find(self, item):
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]  # path halving
            item = self.parent[item]
        return item

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        self.groups -= 1
        return True


def redundant_connection(edges):
    groups = UnionFind(len(edges) + 1)
    for a, b in edges:
        if not groups.union(a, b):
            return [a, b]
    return []


assert redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
uf = UnionFind(5)
uf.union(0, 1)
uf.union(3, 4)
assert uf.groups == 3 and uf.find(0) == uf.find(1) and uf.find(1) != uf.find(3)
```

**Cost:** close to O(1) per operation with path compression and union by rank.

**Mistakes:** comparing items instead of their roots; skipping path compression, which makes long chains slow.

**Practice:** [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/), [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/), [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Shortest paths with weights

**Signals:** the cheapest, fastest, or lowest-effort route when edges have non-negative weights. Use Dijkstra's algorithm. With a limit on the number of stops, use a Bellman-Ford style relaxation.

```python
import heapq
from collections import defaultdict


def dijkstra(edges, source):
    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((end, weight))
    distance = {source: 0}
    heap = [(0, source)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distance.get(node, float("inf")):
            continue  # stale entry; a shorter path was already found
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distance.get(neighbor, float("inf")):
                distance[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return distance


def network_delay(times, nodes, source):
    distance = dijkstra(times, source)
    return max(distance.values()) if len(distance) == nodes else -1


assert network_delay([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
assert network_delay([[1, 2, 1]], 2, 2) == -1
assert dijkstra([(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1)], 0)[3] == 4
```

**Cost:** O(E log V).

**Mistakes:** using Dijkstra's algorithm with negative weights; skipping the stale-entry check, which makes the algorithm slow on dense graphs.

**Practice:** [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/), [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/), [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/), [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

## Backtracking

**Signals:** "all" subsets, permutations, combinations, or valid placements. Build a candidate one choice at a time, recurse, then undo the choice.

```python
def subsets(nums):
    result, path = [], []

    def build(start):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            build(i + 1)
            path.pop()  # undo the choice

    build(0)
    return result


def permutations(nums):
    result, path, used = [], [], [False] * len(nums)

    def build():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(num)
                build()
                path.pop()
                used[i] = False

    build()
    return result


def combination_sum(candidates, target):
    result, path = [], []

    def build(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                path.append(candidates[i])
                build(i, remaining - candidates[i])  # i, not i + 1: reuse allowed
                path.pop()

    build(0, target)
    return result


assert sorted(subsets([1, 2, 3])) == sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
assert len(permutations([1, 2, 3])) == 6
assert sorted(combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
```

**Cost:** exponential, for example O(2ⁿ) subsets or O(n!) permutations. Say this out loud; it is expected.

**Mistakes:** appending `path` instead of a copy of it; forgetting to undo the choice; generating duplicates instead of sorting and skipping equal neighbors.

**Practice:** [78. Subsets](https://leetcode.com/problems/subsets/), [46. Permutations](https://leetcode.com/problems/permutations/), [39. Combination Sum](https://leetcode.com/problems/combination-sum/), [90. Subsets II](https://leetcode.com/problems/subsets-ii/), [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/), [79. Word Search](https://leetcode.com/problems/word-search/), [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/), [51. N-Queens](https://leetcode.com/problems/n-queens/)

## Dynamic programming

**Signals:** "how many ways", "minimum cost", "longest", "can you reach", and a brute force that solves the same subproblem many times. Define the state in words first, for example "best answer for the first i items", then write the transition.

```python
from functools import lru_cache


def climb_stairs(n):
    one_back, two_back = 1, 1
    for _ in range(n - 1):
        one_back, two_back = one_back + two_back, one_back
    return one_back


def coin_change(coins, amount):
    fewest = [0] + [float("inf")] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                fewest[total] = min(fewest[total], fewest[total - coin] + 1)
    return fewest[amount] if fewest[amount] != float("inf") else -1


def longest_common_subsequence(a, b):
    @lru_cache(maxsize=None)
    def best(i, j):  # top-down: LCS of a[i:] and b[j:]
        if i == len(a) or j == len(b):
            return 0
        if a[i] == b[j]:
            return 1 + best(i + 1, j + 1)
        return max(best(i + 1, j), best(i, j + 1))

    return best(0, 0)


def edit_distance(a, b):
    previous = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        current = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                current[j] = previous[j - 1]
            else:
                current[j] = 1 + min(previous[j], current[j - 1], previous[j - 1])
        previous = current
    return previous[-1]


assert climb_stairs(2) == 2 and climb_stairs(5) == 8
assert coin_change([1, 2, 5], 11) == 3
assert coin_change([2], 3) == -1
assert longest_common_subsequence("abcde", "ace") == 3
assert edit_distance("horse", "ros") == 3
assert edit_distance("", "abc") == 3
```

**Cost:** number of states times the work per state, for example O(amount × coins) for coin change.

**Mistakes:** starting to code before you can say what one cell of the table means; wrong base cases; iterating in an order that reads cells you have not filled yet. Start top-down with memoization if bottom-up is unclear. It earns the same credit.

**Practice:** [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/), [198. House Robber](https://leetcode.com/problems/house-robber/), [213. House Robber II](https://leetcode.com/problems/house-robber-ii/), [322. Coin Change](https://leetcode.com/problems/coin-change/), [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/), [139. Word Break](https://leetcode.com/problems/word-break/), [91. Decode Ways](https://leetcode.com/problems/decode-ways/), [62. Unique Paths](https://leetcode.com/problems/unique-paths/), [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/), [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/), [72. Edit Distance](https://leetcode.com/problems/edit-distance/), [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)

## Trie

**Signals:** prefix queries, autocomplete, or searching for many words at once in a grid.

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["$"] = True  # end-of-word marker

    def _walk(self, text):
        node = self.root
        for char in text:
            if char not in node:
                return None
            node = node[char]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and "$" in node

    def starts_with(self, prefix):
        return self._walk(prefix) is not None


trie = Trie()
trie.insert("apple")
assert trie.search("apple")
assert not trie.search("app")
assert trie.starts_with("app")
trie.insert("app")
assert trie.search("app")
```

**Cost:** O(length of the word) per operation.

**Mistakes:** forgetting the end-of-word marker, so prefixes count as words; not pruning found words in Word Search II, which makes it time out.

**Practice:** [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/), [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/), [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

## Greedy

**Signals:** you can argue that taking the locally best option never hurts, for example the interval that ends first or the farthest reachable index. If you cannot explain why the greedy choice is safe, use dynamic programming.

```python
def can_jump(nums):
    farthest = 0
    for i, step in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + step)
    return True


def max_subarray(nums):
    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)  # restart when the running sum hurts
        best = max(best, current)
    return best


assert can_jump([2, 3, 1, 1, 4])
assert not can_jump([3, 2, 1, 0, 4])
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([-3, -1, -2]) == -1
```

**Cost:** usually O(n), or O(n log n) with a sort.

**Mistakes:** applying a greedy rule that only works on the examples. Test it against a small counterexample before you commit.

**Practice:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [55. Jump Game](https://leetcode.com/problems/jump-game/), [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/), [134. Gas Station](https://leetcode.com/problems/gas-station/), [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/), [763. Partition Labels](https://leetcode.com/problems/partition-labels/)

## Bit manipulation

**Signals:** a value that appears an odd number of times, powers of two, or a set of flags small enough to fit in an integer.

```python
from functools import reduce


def single_number(nums):
    return reduce(lambda a, b: a ^ b, nums)  # pairs cancel out


def count_bits(n):
    return bin(n).count("1")


def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0


assert single_number([4, 1, 2, 1, 2]) == 4
assert count_bits(11) == 3
assert is_power_of_two(16) and not is_power_of_two(18) and not is_power_of_two(0)
```

**Cost:** O(n) or O(number of bits).

**Mistakes:** forgetting that Python integers have no fixed width, so problems that assume 32-bit overflow need an explicit mask.

**Practice:** [136. Single Number](https://leetcode.com/problems/single-number/), [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/), [338. Counting Bits](https://leetcode.com/problems/counting-bits/), [268. Missing Number](https://leetcode.com/problems/missing-number/), [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
