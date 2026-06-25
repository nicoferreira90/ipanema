---
title: The Relative Immutability of Tuples
exercise: |
  Write `mutate_inside(t)` where `t` is a tuple whose first item is a list. Append
  `99` to that inner list in place and return `None`. The tuple itself keeps the
  same length and identity.
check: |
  t = ([1, 2], 'x')
  mutate_inside(t)
  assert t == ([1, 2, 99], 'x')
  assert len(t) == 2
---

A tuple is immutable, but it pays to know exactly what that freezes. A tuple fixes
its references, the labels it holds, not the objects those labels point at. You
cannot reassign a slot or change the tuple's length, yet a mutable object stored
inside can still change on its own.

So if `t = ([1, 2], 'x')`, you cannot do `t[0] = []`, but you can do
`t[0].append(99)`, leaving `t` as `([1, 2, 99], 'x')`. The tuple never changed
which objects it references; one of those objects simply changed inside.

This is why a tuple counts as hashable only when everything inside it is hashable.
A tuple holding a list cannot be a dict key or a set member, because its contents
can shift, and a hash that could change underfoot would break the structures that
rely on it.
