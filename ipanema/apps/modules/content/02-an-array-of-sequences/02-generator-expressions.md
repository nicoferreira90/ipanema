---
title: Generator Expressions
exercise: |
  Write a function named `sum_of_squares(n)` that returns the sum of the squares of the numbers
  in `range(n)`. Pass a generator expression straight to `sum()`, with no list
  in between.
check: |
  assert sum_of_squares(4) == 14, "0 + 1 + 4 + 9"
  assert sum_of_squares(1) == 0
  assert sum_of_squares(0) == 0
---

A generator expression looks like a list comprehension but with parentheses,
and it never builds the whole list. It yields items one at a time, so you can
write `total = sum(ord(s) for s in symbols)` to add up code points without an
intermediate list.

When a generator is the sole argument to a function, that function's own
parentheses are enough, so you do not double the `()`. Because it is lazy, a
generator uses almost no memory even for a huge or endless source, since you pay
for one item at a time.

Use a generator when you are feeding another function such as `sum`, `max`,
`any`, or `''.join` and do not need the list itself. If you need to keep, index,
or reuse the result, build a list instead.
