---
title: String Representation
exercise: |
  Give a class `Point(x, y)` a `__repr__` that returns the string
  `'Point(3, 4)'` for `Point(3, 4)` — i.e. it should look like the code that
  would recreate it. Confirm `repr()` round-trips.
check: |
  p = Point(3, 4)
  assert repr(p) == 'Point(3, 4)', "repr should read like Point(3, 4)"
  assert eval(repr(p)).x == 3 and eval(repr(p)).y == 4, "repr should round-trip"
---

When you type an object at the console or log it, Python calls `__repr__`. A
good `__repr__` is **unambiguous** — ideally it looks like the source needed to
rebuild the object:

```python
def __repr__(self):
    return f'Point({self.x!r}, {self.y!r})'
```

The `!r` conversion applies `repr` to each field, so strings keep their quotes
and the result round-trips through `eval`. Contrast `__str__`, used by `print`
and `str()`, which is for friendly human output. If you only write one, write
`__repr__` — Python falls back to it for `str()` too. Without it you get the
unhelpful `<Point object at 0x7f…>`.
