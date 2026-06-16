---
title: Generator Expressions
exercise: |
  Write `sum_of_squares(n)` that returns the sum of the squares of the numbers
  in `range(n)`. Pass a generator expression straight to `sum()` — no list.
check: |
  assert sum_of_squares(4) == 14, "0 + 1 + 4 + 9"
  assert sum_of_squares(1) == 0
  assert sum_of_squares(0) == 0
---

A **generator expression** (*genexp*) looks like a listcomp but with
parentheses — and it never builds the whole list. It yields items one at a
time:

```python
total = sum(ord(s) for s in '$¢£¥€')
```

When a genexp is the sole argument to a function, that function's own
parentheses are enough — no doubled `()`. Because it's lazy, a genexp uses
almost no memory even for a huge or endless source; you pay for one item at a
time. Use a genexp when you're **feeding another function** (`sum`, `max`,
`any`, `''.join`) and don't need the list itself. Need to keep, index, or reuse
the result? Then build a list.
