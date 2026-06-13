---
title: Boolean Value of an Object
exercise: |
  Define `Bag(items)` wrapping a list, with a `__bool__` that is `False` when
  the bag is empty and `True` otherwise. Test it with `bool()` and in an
  `if` statement.
check: |
  assert bool(Bag([])) is False, "an empty Bag should be falsy"
  assert bool(Bag([1])) is True, "a non-empty Bag should be truthy"
  hit = False
  if Bag([1, 2]):
      hit = True
  assert hit, "a non-empty Bag should pass an if test"
---

Every object can be used in a boolean context — `if x:`, `while x:`, `or`,
`and`. By default objects are truthy. To customise this, Python asks two
methods in order:

```python
def __bool__(self):
    return len(self._items) > 0
```

First it tries `__bool__`; if absent, it falls back to `__len__` (zero length
is falsy, non-zero is truthy). So a class that already has `__len__` gets
sensible truthiness for free — just like empty lists, strings, and dicts are
falsy. Defining `__bool__` lets you decide explicitly, and return early without
counting when you can. The rule of thumb: *emptiness is falsiness*.
