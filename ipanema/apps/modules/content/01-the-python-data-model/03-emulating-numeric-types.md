---
title: Emulating Numeric Types
exercise: |
  Define a 2D vector `V2(x, y)` with two special methods: `__add__`, returning
  a new `V2` whose components are the sums, and `__abs__`, returning the
  magnitude (`math.hypot(x, y)`). Test with `+` and `abs()` — not by name.
check: |
  import math
  r = V2(2, 1) + V2(2, 3)
  assert (r.x, r.y) == (4, 4), "__add__ should add componentwise"
  assert isinstance(r, V2), "__add__ should return a new V2"
  assert abs(V2(3, 4)) == 5.0, "__abs__ should return the magnitude"
---

Operators are special methods in disguise. Give a class `__add__` and `__mul__`
and it joins the world of `+` and `*`:

```python
class V2:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return V2(self.x + other.x, self.y + other.y)
    def __abs__(self):
        return math.hypot(self.x, self.y)
```

Two principles worth keeping: operators should **return a new object**, not
mutate `self` — `a + b` shouldn't change `a`. And `abs()`, like `len()`, is a
built-in that simply forwards to your dunder. Your type now reads like maths on
the page while staying ordinary Python underneath.
