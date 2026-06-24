---
title: The Classic namedtuple
exercise: |
  Write `make_point(x, y)` that returns a value with named fields `x` and `y`.
  Define a `Point` type with `collections.namedtuple('Point', ['x', 'y'])` and
  return `Point(x, y)`. The result should support both `p.x` and `p[0]`.
check: |
  p = make_point(3, 4)
  assert p.x == 3
  assert p.y == 4
  assert p[0] == 3
  assert tuple(p) == (3, 4)
---

Sometimes you just need a small bundle of named fields, and writing a full class
with `__init__`, `__repr__`, and `__eq__` by hand is a lot of ceremony for that.
`collections.namedtuple` writes that code for you.

You call it with a type name and the field names, as in
`Point = namedtuple('Point', 'x y')`. Now `Point` is a class. Create an instance
with `Point(3, 4)`, then read fields by name with `p.x` or by position with
`p[0]`, since a namedtuple is a real tuple underneath.

That tuple nature is the whole point. Instances are immutable, they unpack with
`x, y = p`, and they compare and hash like any tuple. You get readable attribute
access and a tidy repr like `Point(x=3, y=4)` for free, all from a single line of
definition.
