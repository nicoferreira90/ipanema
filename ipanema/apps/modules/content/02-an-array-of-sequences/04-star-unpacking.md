---
title: Star Unpacking
exercise: |
  Write `head_tail(seq)` that returns a `(first, rest)` tuple. `first` is the
  first item and `rest` is a list of everything after it. Use a starred target
  to do this, not slicing.
check: |
  assert head_tail([1, 2, 3, 4]) == (1, [2, 3, 4])
  assert head_tail([9]) == (9, [])
  assert head_tail('abc') == ('a', ['b', 'c'])
---

One target in an unpacking can be starred to grab the leftovers as a list. In
`first, *rest = [1, 2, 3, 4]`, `first` is `1` and `rest` is `[2, 3, 4]`. The
star can sit anywhere, so `*init, last = [1, 2, 3, 4]` gives `init` as
`[1, 2, 3]` and `last` as `4`, while `a, *mid, z = range(6)` puts the middle
values in `mid`.

The starred name soaks up whatever is left, zero or more items, and is always
bound to a list. Only one star is allowed per assignment. The same `*` also
splats an iterable into a function call, as in `print(*tags)`, or into a new
list, as in `[*a, *b]`. It is the readable way to peel off the parts you care
about and keep the rest in one move.
