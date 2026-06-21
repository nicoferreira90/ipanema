---
title: The Collection API & Recap
exercise: |
  Define `Ring(items)` that wraps a list and implements the three core
  collection methods: `__len__` for Sized, `__iter__` for Iterable, and
  `__contains__` for Container. Have all three delegate to the wrapped list.
check: |
  r = Ring([10, 20, 30])
  assert len(r) == 3, "Sized: __len__"
  assert list(r) == [10, 20, 30], "Iterable: __iter__"
  assert (20 in r) and (99 not in r), "Container: __contains__"
---

The special methods you have met cluster into the collection API. Three core
protocols sit at its heart:

- Sized, through `__len__`, so `len(x)` works.
- Iterable, through `__iter__`, so `for` loops and unpacking work.
- Container, through `__contains__`, so `in` works.

To support the last two, an object can give `__iter__(self)` returning
`iter(self._items)` and `__contains__(self, value)` returning
`value in self._items`.

Implement these explicitly and your object is a first-class citizen alongside
`list`, `tuple`, and `set`. That is the chapter's lesson: Python defines
behaviour through protocols, not inheritance. Match the protocol and the
language treats your object as one of its own. Next you will fold these ideas
into a complete `Vector`.
