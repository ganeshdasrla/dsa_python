# Learning path

For each topic: explain the idea, trace a small example on paper, implement it,
test empty and boundary cases, then write down time and space complexity.

| Order | Topic | Practice |
| --- | --- | --- |
| 1 | Python basics and Big O | Lists, loops, functions, dictionaries; compare O(1), O(n), O(log n) |
| 2 | Searching | Trace linear and binary searches; implement first occurrence |
| 3 | Sorting | Trace bubble sort; add insertion sort and merge sort |
| 4 | Arrays and strings | Two sum, two pointers, sliding window, palindrome |
| 5 | Stack and queue | Use the stack; balanced brackets; queue using collections.deque |
| 6 | Linked lists | Insert, delete, reverse, find the middle |
| 7 | Recursion | Factorial, subsets, base cases and the call stack |
| 8 | Trees | Traversals, binary search tree lookup, height |
| 9 | Graphs | Adjacency lists, BFS, DFS, visited sets |
| 10 | Dynamic programming | Memoized Fibonacci, climbing stairs, coin change |

## First debugging exercise

1. Open `src/dsa_python/searching.py` and set a breakpoint on `middle = ...`.
2. Press F5 and select **Run DSA demo**. The demo calls your algorithm.
3. Add `left`, `right`, `middle`, and `target` to the Watch panel.
4. Press F10 (Step Over) and observe how the search interval shrinks.
5. Press F11 (Step Into) at a function call to enter that function.
6. Press F5 (Continue) to finish. Try a missing target and an empty list.

Algorithm modules define functions, so running a module alone produces no demo
output. Start the demo or debug a test to exercise those functions.

## Practice log

Copy this template into your notes for each problem:

```text
Problem:
Example input and expected output:
Approach:
Edge cases:
Time complexity:
Space complexity:
What I learned:
```
