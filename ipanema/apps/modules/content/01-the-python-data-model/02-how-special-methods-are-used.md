---
title: How Special Methods Are Used
exercise: |
  Define `Squares(n)` whose `__getitem__(i)` returns `i * i` and whose
  `__len__` returns `n`. Don't write an `__iter__` or `__contains__` — confirm
  that iteration and the `in` operator come for free from `__getitem__`.
check: |
  sq = Squares(5)
  assert list(sq) == [0, 1, 4, 9, 16], "iteration falls out of __getitem__"
  assert 9 in sq, "'in' falls out of __getitem__ too"
  assert 7 not in sq, "and reports missing values correctly"
---

A key idea: **you rarely call special methods yourself.** You call `len(x)`,
not `x.__len__()`; you write `x + y`, not `x.__add__(y)`. The interpreter
invokes the dunder for you — and for built-in types it may even take a
shortcut straight to C.

The payoff is consistency. Implement `__getitem__` alone and Python can:

```python
for item in obj:      # iterate, indexing 0, 1, 2…
value in obj          # membership test
```

Both are *fallbacks* built on top of `__getitem__`. So one method quietly
unlocks several behaviours. This is why "Pythonic" code leans on the data
model: you opt into a protocol, and the language meets you with everything
that protocol implies.
