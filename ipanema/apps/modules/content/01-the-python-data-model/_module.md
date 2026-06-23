---
title: The Python Data Model
part: "Part I: Data Structures"
tagline: Dunder methods & the secret life of objects
color: coral
status: available
project:
  title: A Pythonic 2D Vector
  placeholder: "# build your Vector class here"
  brief: |
    Write a `Vector` class for 2D vectors that feels native to Python. The
    interpreter should do the work through your special methods, not through
    methods you call by name.

    Your `Vector` must support:

    - `Vector(3, 4)` stores `x` and `y`.
    - `repr(v)` gives the string `'Vector(3, 4)'`, which round-trips to source.
    - `abs(v)` gives the magnitude, `math.hypot(x, y)`.
    - `v1 + v2` gives a new `Vector` whose components are the two added together.
    - `v * n` scales by a number and returns a new `Vector`.
    - `v1 == v2` is `True` when both components match.
    - `bool(v)` is `False` only for the zero vector.

    Do not call any dunder directly in your tests. Use `+`, `*`, `==`, `abs`,
    `repr`, and `bool`, and let Python dispatch. Aim for about 15 to 20 lines.
  check: |
    import math
    v = Vector(3, 4)
    assert repr(v) == 'Vector(3, 4)', "repr should be 'Vector(3, 4)'"
    assert abs(v) == 5.0, "abs(Vector(3, 4)) should be 5.0"
    assert v + Vector(1, 2) == Vector(4, 6), "addition is componentwise"
    assert v * 3 == Vector(9, 12), "v * n scales both components"
    assert (v == Vector(3, 4)) is True, "equal vectors compare equal"
    assert (v == Vector(0, 0)) is False, "different vectors are not equal"
    assert bool(Vector(0, 0)) is False, "the zero vector is falsy"
    assert bool(v) is True, "a non-zero vector is truthy"
---

Six short lessons on how Python objects talk to the language itself. Build them
up one special method at a time, then assemble a `Vector` that behaves like a
built-in.
