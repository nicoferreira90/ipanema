---
title: Tuples as Records & Unpacking
exercise: |
  Write `midpoint(p1, p2)` where each point is an `(x, y)` tuple. Unpack both
  points and return the midpoint as a new `(x, y)` tuple. (Averaging gives
  floats, e.g. `2.0`.)
check: |
  assert midpoint((0, 0), (4, 2)) == (2.0, 1.0)
  assert midpoint((1, 1), (1, 1)) == (1.0, 1.0)
---

A tuple is more than an immutable list — it's often a **record**, where each
position carries meaning:

```python
lax = (33.94, -118.40)
city, year, pop = ('Tokyo', 2003, 32_450)
```

That second line is **unpacking**: Python matches the items on the right to the
names on the left, by position. It powers the clean swap

```python
a, b = b, a
```

and lets a function return several values as a tuple the caller pulls apart.
Unpacking works on any iterable, and you can discard items you don't want with
a dummy `_`: `name, _ = record`. Prefer unpacking to `record[0]`, `record[1]` —
names read far better than indexes.
