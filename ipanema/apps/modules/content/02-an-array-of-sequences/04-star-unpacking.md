---
title: Star Unpacking
exercise: |
  Write `head_tail(seq)` that returns a `(first, rest)` tuple: the first item,
  and a list of everything after it. Use a starred target — no slicing.
check: |
  assert head_tail([1, 2, 3, 4]) == (1, [2, 3, 4])
  assert head_tail([9]) == (9, [])
  assert head_tail('abc') == ('a', ['b', 'c'])
---

One target in an unpacking can be **starred** to grab the leftovers as a list:

```python
first, *rest = [1, 2, 3, 4]      # first=1, rest=[2, 3, 4]
*init, last = [1, 2, 3, 4]       # init=[1, 2, 3], last=4
a, *mid, z = range(6)            # a=0, mid=[1, 2, 3, 4], z=5
```

The starred name soaks up whatever is left — zero or more items — and is always
bound to a **list**. Only one star is allowed per assignment, but it can sit
anywhere. The same `*` splats an iterable into a function call,
`print(*tags)`, or into a new list, `[*a, *b]`. It's the readable way to peel
off the parts you care about and keep the rest in one move.
