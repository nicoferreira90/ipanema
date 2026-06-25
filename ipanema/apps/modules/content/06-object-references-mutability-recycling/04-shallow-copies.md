---
title: Shallow Copies
exercise: |
  Write `shallow(lst)` that returns a shallow copy of `lst`: a new list holding
  the same items. The result should equal `lst` but not be the same object, while
  the inner items stay shared.
check: |
  original = [[1], [2]]
  dup = shallow(original)
  assert dup == original
  assert dup is not original
  assert dup[0] is original[0]
---

To stop sharing, you make a copy. The quickest ways, `list(x)`, `x[:]`, and
`copy.copy(x)`, all build a new outer list. That solves half the problem.

The catch is that the copy is shallow. The new list is its own object, but it is
filled with the same inner objects as the original, not copies of them. So adding
or removing items at the top level is independent between the two lists, yet
reaching into a shared inner object and mutating it shows up in both. If
`a = [[1], [2]]` and `b = a[:]`, then `b.append([3])` leaves `a` alone, but
`b[0].append(99)` also changes `a[0]`, because `a[0]` and `b[0]` are the same list.

Shallow copying is the default and usually enough. Just remember it duplicates one
layer, not the whole nested structure.
