---
title: List Comprehensions
exercise: |
  Write a function named `squares_of_evens(n)` that returns a list with the squares of the even
  numbers in `range(n)`. Build it with a single list comprehension.
check: |
  assert squares_of_evens(6) == [0, 4, 16], "0, 2, 4 squared"
  assert squares_of_evens(1) == [0], "just 0"
  assert squares_of_evens(0) == [], "empty range -> empty list"
---

A list comprehension builds a list from an iterable in one expression. It says
what you want instead of the bookkeeping of a `for` loop with `.append()`. To
collect the code points of some symbols you would write
`codes = [ord(s) for s in symbols]`.

Add an `if` to filter, as in `[ord(s) for s in symbols if ord(s) > 127]`. Read
it left to right: an output expression, a `for`, then optional `if` clauses.

Comprehensions have their own local scope, so the loop variable does not leak
out and clobber a name outside. Reach for one when the goal is to build a list.
If you are looping purely for side effects, keep the plain `for`.
