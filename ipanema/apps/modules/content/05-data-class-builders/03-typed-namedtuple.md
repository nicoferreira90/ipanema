---
title: Typed NamedTuple
exercise: |
  Define a typed NamedTuple named `Coordinate` with two fields, `lat` and `lon`,
  both hinted as `float`, using the class form. It should be created as
  `Coordinate(40.7, -74.0)`. Remember to import `NamedTuple` from `typing`.
check: |
  c = Coordinate(40.7, -74.0)
  assert c.lat == 40.7
  assert c.lon == -74.0
  assert isinstance(c, tuple)
---

`typing.NamedTuple` builds the very same kind of immutable, tuple-based record,
but with a cleaner class syntax and a type hint on every field.

You write it as a class that inherits from `NamedTuple` and lists each field as
`name: type`. A point becomes `class Point(NamedTuple):` with `x: int` and
`y: int` on the lines below. You create and use it exactly as before, with
`Point(3, 4)`, `p.x`, and unpacking.

The result is still a tuple, so everything you learned about namedtuple still
holds, including `_fields`, `_asdict`, and `_replace`. You can also add methods
and per-field defaults right in the class body. This is the form to prefer when
you want your fields documented with their types and your editor helping you as
you go.
