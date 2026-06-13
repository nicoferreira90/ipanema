---
title: The Collection API & Recap
exercise: |
  Define `Ring(items)` that wraps a list and implements the three collection
  pillars explicitly: `__len__` (Sized), `__iter__` (Iterable), and
  `__contains__` (Container). Make all three delegate to the wrapped list.
check: |
  r = Ring([10, 20, 30])
  assert len(r) == 3, "Sized: __len__"
  assert list(r) == [10, 20, 30], "Iterable: __iter__"
  assert (20 in r) and (99 not in r), "Container: __contains__"
---

The special methods you've met cluster into the **collection API**. Three
core protocols sit at its heart:

- **Sized** — `__len__`, so `len(x)` works.
- **Iterable** — `__iter__`, so `for` loops and unpacking work.
- **Container** — `__contains__`, so `in` works.

```python
def __iter__(self):
    return iter(self._items)
def __contains__(self, value):
    return value in self._items
```

Implement these explicitly and your object is a first-class citizen alongside
`list`, `tuple`, and `set`. That's the chapter's lesson: Python defines
behaviour through protocols, not inheritance. Match the protocol and the
language treats your object as one of its own. Next, you'll fold these ideas
into a complete `Vector`.
