---
title: Identity vs Equality
exercise: |
  Write `describe(a, b)` that returns the two-item tuple `(a == b, a is b)`: first
  whether the two values are equal, then whether they are the same object.
check: |
  x = [1, 2]
  y = [1, 2]
  assert describe(x, y) == (True, False)
  z = x
  assert describe(x, z) == (True, True)
---

Two objects can be equal without being the same object, so Python gives you two
different questions to ask.

`==` compares values. It calls the object's `__eq__` method and answers whether
the contents match, so `[1, 2] == [1, 2]` is `True` even though those are two
separate lists. `is` compares identity. It answers whether two names point at the
exact same object, the same one you would see from `id()`.

Almost always you want `==`, because you care about the value, not the storage.
The classic exception is comparing against a singleton: write `x is None`, never
`x == None`, since there is only ever one `None` and identity is the precise check.
Two equal lists living at different addresses are equal but not identical, and
keeping that distinction clear saves you from puzzling bugs.
