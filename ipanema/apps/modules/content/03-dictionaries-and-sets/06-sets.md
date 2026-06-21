---
title: Sets & Set Operations
exercise: |
  Write `common(a, b)` that returns a sorted list of the values found in
  **both** lists `a` and `b`, with no duplicates. Use set operations.
check: |
  assert common([1, 2, 3, 2], [2, 3, 4]) == [2, 3]
  assert common([1], [2]) == []
---

A set is an unordered collection of distinct, hashable items. Building one drops
duplicates for free, so `set([1, 2, 2, 3])` becomes `{1, 2, 3}`.

Sets speak the language of algebra through operators. `a | b` is the union, the
items in either set. `a & b` is the intersection, the items in both. `a - b` is
the difference, the items in `a` but not `b`. `a ^ b` is the symmetric
difference, the items in one set but not both.

Membership tests like `x in s` are near-instant, far faster than scanning a
list. Sets are mutable. If you need a hashable, frozen one, for example as a
dict key, use `frozenset`. Reach for a set whenever you care about uniqueness or
membership rather than order or position.
