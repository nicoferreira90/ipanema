---
title: The __missing__ Method
exercise: |
  Write a `dict` subclass `ZeroDict` where missing keys read as `0` instead of
  raising an error. Looking up an absent key returns `0`, but that key must not
  be added to the dict.
check: |
  z = ZeroDict(a=1)
  assert z['a'] == 1
  assert z['x'] == 0, "missing key reads as 0"
  assert 'x' not in z, "__missing__ must not insert the key"
---

When you subclass `dict`, you can define `__missing__(self, key)`, and Python
calls it automatically whenever `d[key]` fails to find the key. A subclass whose
`__missing__` returns `0` turns every absent key into a zero.

Now `ZeroDict(a=1)['x']` returns `0` rather than raising `KeyError`. Two things
are worth knowing. `__missing__` is triggered only by `d[key]` indexing, not by
`.get()` and not by the `in` operator, so `'x' in z` is still `False`. And
whatever you return is not stored unless you put it there yourself. It is the
hook that `defaultdict` is built on, exposed for you to customise.
