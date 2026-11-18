# Fundamentals

The reference tables and language tools you should know cold before a coding round. If any row here surprises you, study that topic before moving on to [coding patterns](coding-patterns.md).

## Contents

- [Read the constraints first](#read-the-constraints-first)
- [Data structure costs](#data-structure-costs)
- [Sorting](#sorting)
- [Graph algorithms](#graph-algorithms)
- [Python toolkit](#python-toolkit)
- [Choosing a language](#choosing-a-language)
- [Where to learn more](#where-to-learn-more)

## Read the constraints first

The input size in the problem statement tells you roughly how fast your solution must be. A typical judge runs about 10⁸ simple operations per second, so:

| Input size `n` | Target complexity | Typical approach |
| --- | --- | --- |
| up to 10 | O(n!) | Permutations, brute force |
| up to 20 | O(2ⁿ) | Subsets, bitmask search |
| up to 500 | O(n³) | Triple loops, interval DP |
| up to 5,000 | O(n²) | Nested loops, 2D DP |
| up to 10⁶ | O(n log n) | Sorting, heaps, binary search |
| above 10⁶ | O(n) or O(log n) | Single pass, hashing, math |

In an interview, ask about input size before you design. It is a cheap question that interviewers like.

## Data structure costs

Average case unless noted. Python names are given because most candidates use Python.

| Structure | Access | Search | Insert | Delete | Python |
| --- | --- | --- | --- | --- | --- |
| Dynamic array | O(1) | O(n) | O(1) amortized at end, O(n) elsewhere | O(1) at end, O(n) elsewhere | `list` |
| Linked list | O(n) | O(n) | O(1) at a known node | O(1) at a known node | write your own |
| Hash map / set | n/a | O(1), O(n) worst | O(1) | O(1) | `dict`, `set` |
| Stack | O(1) top | O(n) | O(1) | O(1) | `list` with `append`/`pop` |
| Queue / deque | O(1) ends | O(n) | O(1) at either end | O(1) at either end | `collections.deque` |
| Binary heap | O(1) min | O(n) | O(log n) | O(log n) min | `heapq` |
| Balanced BST | O(log n) | O(log n) | O(log n) | O(log n) | none built in; use `bisect` on a sorted list for small inputs |
| Trie | n/a | O(length) | O(length) | O(length) | nested `dict` |
| Union-find | n/a | ~O(1) find | ~O(1) union | n/a | write your own |

## Sorting

| Algorithm | Best | Average | Worst | Extra space | Stable |
| --- | --- | --- | --- | --- | --- |
| Timsort (Python `sorted`, Java objects) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |

You will rarely write a sort in an interview, but you may be asked how one works or why quicksort's worst case happens: a bad pivot on already-sorted input.

## Graph algorithms

| Problem | Algorithm | Cost |
| --- | --- | --- |
| Reachability, connected components | Depth-first or breadth-first search | O(V + E) |
| Shortest path, unweighted | Breadth-first search | O(V + E) |
| Shortest path, non-negative weights | Dijkstra's algorithm | O(E log V) |
| Shortest path, negative weights or at most K edges | Bellman-Ford | O(V × E) |
| All-pairs shortest paths, small graph | Floyd-Warshall | O(V³) |
| Dependency order, cycle detection in a directed graph | Topological sort | O(V + E) |
| Minimum spanning tree | Kruskal's with union-find, or Prim's with a heap | O(E log E) |

Templates for most of these are in [coding patterns](coding-patterns.md).

## Python toolkit

These standard-library tools turn ten lines into one and are allowed in every interview.

```python
import bisect
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import accumulate, combinations, pairwise, permutations

# Counting and grouping
assert Counter("banana").most_common(1) == [("a", 3)]
groups = defaultdict(list)
for word in ["eat", "tea", "tan", "ate"]:
    groups["".join(sorted(word))].append(word)
assert groups["aet"] == ["eat", "tea", "ate"]

# Queue with O(1) at both ends
queue = deque([1, 2, 3])
queue.appendleft(0)
assert queue.popleft() == 0 and queue.pop() == 3

# Min-heap; negate values for a max-heap
heap = [5, 1, 8]
heapq.heapify(heap)
assert heapq.heappop(heap) == 1
assert heapq.nlargest(2, [5, 1, 8, 3]) == [8, 5]

# Binary search on a sorted list
scores = [10, 20, 20, 30]
assert bisect.bisect_left(scores, 20) == 1   # first index >= 20
assert bisect.bisect_right(scores, 20) == 3  # first index > 20

# Memoization in one line
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

assert fib(50) == 12586269025

# Running totals, pairs, and combinations
assert list(accumulate([1, 2, 3])) == [1, 3, 6]
assert list(pairwise([1, 2, 3])) == [(1, 2), (2, 3)]
assert len(list(combinations(range(4), 2))) == 6
assert len(list(permutations("abc"))) == 6

# Sorting by several keys: highest score first, then name
people = [("bo", 90), ("al", 90), ("cy", 70)]
assert sorted(people, key=lambda p: (-p[1], p[0])) == [("al", 90), ("bo", 90), ("cy", 70)]

# Infinity and integer limits
assert float("inf") > 10**18
assert (2**31 - 1) == 2147483647
```

`itertools.pairwise` needs Python 3.10 or later. Check which version the interview platform runs.

## Choosing a language

Use the language you write fastest and most accurately. Python is the most common choice because it is short to write, but interviewers at large companies accept any mainstream language. Whatever you pick:

- Know how to declare a hash map, a heap, a queue, and a sorted structure without looking it up.
- Know your language's integer overflow behavior and its recursion limits. Python's default recursion limit is 1,000 frames, which deep tree or grid problems can exceed.
- Practise in a plain editor with no autocomplete, since many interviews use one.

## Where to learn more

See [Data Structures and Algorithms](../README.md#data-structures-and-algorithms) in the main list for courses, visualizations, and books.
