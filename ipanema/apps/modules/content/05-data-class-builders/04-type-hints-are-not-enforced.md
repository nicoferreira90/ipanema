---
title: Type Hints Are Not Enforced
exercise: |
  Write `annotation_names(cls)` that returns a list of the annotated field names
  of a class, in order, by reading its `__annotations__` dict.
check: |
  class Book:
      title: str
      pages: int
  assert annotation_names(Book) == ['title', 'pages']
  class User:
      name: str
      age: int
      active: bool
  assert annotation_names(User) == ['name', 'age', 'active']
---

The type hints you just wrote are documentation, not rules. Python does not check
them at runtime, so nothing stops you from putting a string where an `int` was
annotated. A hint like `lat: float` states what you intend, and your editor and
tools like `mypy` use it to warn you, but the interpreter itself never enforces
it.

Where do the hints go? Python collects them into a class attribute called
`__annotations__`, a plain dict mapping each field name to its hinted type. You
can read it like any dict, so `Point.__annotations__` might be
`{'x': int, 'y': int}`. That is all an annotation really is: a piece of stored
data.

So lean on hints for clarity and tooling, but remember the values you actually
pass are still your own responsibility at runtime.
