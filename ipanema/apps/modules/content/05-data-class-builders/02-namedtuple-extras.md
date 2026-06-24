---
title: namedtuple's Extra Methods
exercise: |
  Write `as_dict(record)` that takes any namedtuple instance and returns an
  ordinary dict mapping its field names to their values. Use the `_asdict`
  method.
check: |
  from collections import namedtuple
  Point = namedtuple('Point', 'x y')
  assert as_dict(Point(1, 2)) == {'x': 1, 'y': 2}
  Color = namedtuple('Color', 'r g b')
  assert as_dict(Color(10, 20, 30)) == {'r': 10, 'g': 20, 'b': 30}
---

Beyond plain tuple behaviour, every namedtuple carries a few extra helpers, each
named with a leading underscore so it never clashes with your own field names.

`_fields` is a tuple of the field names, handy when you want to inspect a type.
`_asdict()` turns an instance into an ordinary dict, perfect for handing a record
to JSON. `_replace()` makes a new instance with some fields changed, leaving the
original untouched, since namedtuples are immutable. `_make(iterable)` builds an
instance from a sequence, the mirror image of unpacking.

You can also give fields defaults with the `defaults` argument, which fills from
the rightmost field, as in `namedtuple('Point', 'x y', defaults=[0])`. That lets
`Point(5)` mean `Point(5, 0)`. Together these extras make namedtuple a small but
complete record type.
