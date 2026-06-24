---
title: The @dataclass Decorator
exercise: |
  Use `@dataclass` to define a class `Dog` with fields `name` (a `str`) and `age`
  (an `int`). The decorator should generate `__init__`, `__repr__`, and `__eq__`
  for you, and instances should be mutable. Import `dataclass` from `dataclasses`.
check: |
  d = Dog('Rex', 5)
  assert d.name == 'Rex'
  assert d.age == 5
  assert d == Dog('Rex', 5)
  assert d != Dog('Rex', 6)
  d.age = 6
  assert d.age == 6
---

The third builder, `@dataclass` from the `dataclasses` module, decorates a normal
class and writes the boilerplate for you, but the result is a regular object, not
a tuple.

You list each field as an annotated attribute in the class body, the same
`name: type` form, and the decorator generates `__init__`, `__repr__`, and
`__eq__` to match. A `Dog` with `name: str` and `age: int` then supports
`Dog('Rex', 5)`, prints as `Dog(name='Rex', age=5)`, and compares equal field by
field.

The big difference from the tuple builders is mutability: by default a dataclass
instance lets you reassign fields, so `d.age = 6` just works. It is also a plain
class, so it is free to grow methods and properties of its own. This is the most
flexible of the three builders.
