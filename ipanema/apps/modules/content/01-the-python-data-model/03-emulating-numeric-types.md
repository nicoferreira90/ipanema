---
title: Emulating Numeric Types
exercise: |
  Define a 2D vector `V2(x, y)` with two special methods. `__add__` returns a
  new `V2` whose components are the two vectors added together. `__abs__`
  returns the magnitude, which is `math.hypot(x, y)`.
check: |
  import math
  r = V2(2, 1) + V2(2, 3)
  assert (r.x, r.y) == (4, 4), "__add__ should add componentwise"
  assert isinstance(r, V2), "__add__ should return a new V2"
  assert abs(V2(3, 4)) == 5.0, "__abs__ should return the magnitude"
---

Operators are special methods in disguise. Give a class an `__add__` and an
`__abs__` and it joins the world of `+` and `abs()`. A 2D vector might define
`__add__(self, other)` to return `V2(self.x + other.x, self.y + other.y)`, and
`__abs__(self)` to return `math.hypot(self.x, self.y)`.

Two principles are worth keeping. Operators should return a new object rather
than mutate `self`, so `a + b` does not change `a`. And `abs()`, like `len()`,
is a built-in that simply forwards to your dunder. Your type now reads like
maths on the page while staying ordinary Python underneath.
