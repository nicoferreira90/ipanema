---
title: How Special Methods Are Used
exercise: |
  Make a class `Roster` that wraps a list of names passed to `__init__`.
  Implement `__len__` so `len(roster)` gives the number of names, and
  `__getitem__` so `roster[i]` returns the name at index `i`. Do not write
  `__iter__` or `__contains__`. Because Python builds both on top of
  `__getitem__`, looping over the roster and using `in` will just work.
check: |
  r = Roster(['Ana', 'Beto', 'Cira'])
  assert len(r) == 3, "len comes from __len__"
  assert r[0] == 'Ana', "indexing comes from __getitem__"
  assert [name for name in r] == ['Ana', 'Beto', 'Cira'], "iteration is free"
  assert 'Beto' in r, "membership is free"
  assert 'Zed' not in r, "a missing name is reported correctly"
---

A key idea is that you rarely call special methods yourself. You call `len(x)`,
not `x.__len__()`, and you write `x + y`, not `x.__add__(y)`. The interpreter
invokes the dunder for you, and for built-in types it may even take a shortcut
straight to C.

The payoff is consistency. Implement `__getitem__` alone and Python can already
loop over your object with `for item in obj` and test membership with
`value in obj`. Both behaviours fall back to `__getitem__`, so one method
quietly unlocks several.

This is why Pythonic code leans on the data model. You opt into a protocol, and
the language meets you with everything that protocol implies.
