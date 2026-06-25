---
title: Aliasing and Mutation
exercise: |
  Write `add_item(box, item)` that appends `item` to the list `box` in place and
  returns `None`. Because `box` is the caller's list, the change should be visible
  to every name pointing at it.
check: |
  shared = [1, 2]
  also = shared
  add_item(shared, 3)
  assert shared == [1, 2, 3]
  assert also == [1, 2, 3]
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
