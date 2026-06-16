---
title: List Comprehensions
exercise: |
  Write `squares_of_evens(n)` that returns a list of the squares of the even
  numbers in `range(n)` — build it with a single list comprehension.
check: |
  assert squares_of_evens(6) == [0, 4, 16], "0, 2, 4 squared"
  assert squares_of_evens(1) == [0], "just 0"
  assert squares_of_evens(0) == [], "empty range -> empty list"
---

A **list comprehension** (*listcomp*) builds a list from an iterable in one
expression — saying *what* you want, not the bookkeeping of a `for` loop with
`.append()`:

```python
symbols = '$¢£¥€'
codes = [ord(s) for s in symbols]
```

Add an `if` to filter:

```python
big = [ord(s) for s in symbols if ord(s) > 127]
```

Read it left to right: an output expression, a `for`, then optional `if`s.
Listcomps have their own local scope, so the loop variable won't leak out and
clobber a name outside. Reach for one when the goal is to **build a list**; if
you're looping purely for side effects, keep the plain `for`.
