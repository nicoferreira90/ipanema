---
title: Boolean Value of an Object
exercise: |
  Define `Bag(items)` that wraps a list. Add a `__bool__` that returns `False`
  when the bag is empty and `True` otherwise. Test it with `bool()` and inside
  an `if` statement.
check: |
  assert bool(Bag([])) is False, "an empty Bag should be falsy"
  assert bool(Bag([1])) is True, "a non-empty Bag should be truthy"
  hit = False
  if Bag([1, 2]):
      hit = True
  assert hit, "a non-empty Bag should pass an if test"
---

Every object can be used in a boolean context, such as `if x:`, `while x:`,
`or`, and `and`. By default objects are truthy. To customise this, Python asks
two methods in order. You might give a class a `__bool__(self)` that returns
`len(self._items) > 0`.

First it tries `__bool__`. If that is absent, it falls back to `__len__`, where
zero length is falsy and non-zero is truthy. So a class that already has
`__len__` gets sensible truthiness for free, just as empty lists, strings, and
dicts are falsy. Defining `__bool__` lets you decide explicitly and return early
without counting. The rule of thumb is that emptiness is falsiness.
