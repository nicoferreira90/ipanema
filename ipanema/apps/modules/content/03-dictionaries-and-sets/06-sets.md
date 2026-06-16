---
title: Sets & Set Operations
exercise: |
  Write `common(a, b)` that returns a sorted list of the values found in
  **both** lists `a` and `b`, with no duplicates. Use set operations.
check: |
  assert common([1, 2, 3, 2], [2, 3, 4]) == [2, 3]
  assert common([1], [2]) == []
---

A **set** is an unordered collection of distinct, hashable items. Building one
drops duplicates for free:

```python
unique = set([1, 2, 2, 3])     # {1, 2, 3}
```

Sets speak the language of algebra through operators:

```python
a | b      # union — in either
a & b      # intersection — in both
a - b      # difference — in a but not b
a ^ b      # symmetric difference — in one, not both
```

Membership tests (`x in s`) are near-instant, far faster than scanning a list.
Sets are mutable; need a hashable, frozen one — say, as a dict key? Use
`frozenset`. Reach for a set whenever you care about *uniqueness* or
*membership* rather than order or position.
