---
title: Aliasing and Mutation
exercise: |
  Write a function `alias_vs_rebind(numbers)` that shows the difference between
  mutating a shared object and rebinding a name. Inside the function, first make a
  second name for the same list with `same = numbers` (an alias, not a copy).
  Append `99` to the list through `same`. Then rebind that name with `same = [0]`,
  which points `same` at a brand new list. Finally, return `numbers`.

  Because the append went through an alias of the same object, `numbers` ends up
  with `99` added. Because the rebinding only moved the `same` label, the `[0]`
  never touches `numbers`.
check: |
  n = [1, 2]
  out = alias_vs_rebind(n)
  assert out == [1, 2, 99]
  assert n == [1, 2, 99]
  assert out is n
---

Aliases are harmless until something changes. When two names point at the same
mutable object, a mutation made through one name is seen through the other,
because there is only one object to begin with.

So if `a = [1, 2]` and `b = a`, then `a.append(3)` leaves both `a` and `b` reading
`[1, 2, 3]`. You did not touch `b`, but `b` was never a copy. This is the source
of many surprises: a list handed to a function, stored in two places, or shared
across objects can change underfoot.

Mutating in place is different from rebinding. `a.append(3)` changes the shared
object, but `a = [9]` only moves the label `a`, leaving `b` on the original. Knowing
which one you are doing tells you whether other names will notice.
