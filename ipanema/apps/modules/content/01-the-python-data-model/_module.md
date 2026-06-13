---
title: The Python Data Model
part: Part I — Data Structures
tagline: Dunder methods & the secret life of objects
color: coral
status: available
project:
  title: A Pythonic 2D Vector
  brief: |
    Tie the whole chapter together. Write a `Vector` class for 2D vectors that
    feels native to Python — the interpreter should do the work through your
    special methods, not through named helpers.

    Your `Vector` must support:

    - `Vector(3, 4)` — store `x` and `y`.
    - `repr(v)` → the string `'Vector(3, 4)'` (round-trips to source).
    - `abs(v)` → the magnitude, `math.hypot(x, y)`.
    - `v1 + v2` → a new `Vector` of the component sums.
    - `v * n` → scale by a number, returning a new `Vector`.
    - `v1 == v2` → `True` when both components match.
    - `bool(v)` → `False` only for the zero vector.

    Don't call any dunder directly in your tests — use `+`, `*`, `==`, `abs`,
    `repr`, `bool` and let Python dispatch. ~15–20 lines.
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
