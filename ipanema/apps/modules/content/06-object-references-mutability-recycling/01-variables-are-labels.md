---
title: Variables Are Labels
exercise: |
  Write `is_alias(a, b)` that returns `True` when `a` and `b` are two names for
  the very same object, and `False` otherwise. Use `is`.
check: |
  x = [1, 2]
  y = x
  assert is_alias(x, y) is True
  z = [1, 2]
  assert is_alias(x, z) is False
---

A variable in Python is not a box that holds a value. It is a label tied to an
object. When you write `a = [1, 2]`, the list is the object and `a` is just a name
pointing at it.

That difference matters the moment you assign one name to another. `b = a` does
not copy the list. It sticks a second label on the same object, so now `a` and `b`
are aliases for one list. Reassigning a name, as in `a = [9]`, only moves that one
label to a different object and leaves the other name where it was.

To ask whether two names point at the same object, use `is`. It checks identity,
not contents, which is exactly the question of whether you are looking at one
object through two labels.
