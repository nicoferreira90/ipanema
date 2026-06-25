---
title: Deep Copies
exercise: |
  Write `deep(lst)` that returns a deep copy of `lst` using `copy.deepcopy`, so the
  result shares none of its inner objects with the original.
check: |
  original = [[1], [2]]
  dup = deep(original)
  dup[0].append(99)
  assert original[0] == [1]
  assert dup[0] == [1, 99]
---

When a shallow copy is not enough, reach for `copy.deepcopy`. It copies the outer
object and then walks into every object it contains, copying those too, all the
way down. The result shares nothing with the original, so you can mutate the deep
copy freely without the original ever noticing.

Use it when you hold a nested structure, like a list of lists or a dict of dicts,
and you truly need an independent duplicate. A snapshot you can roll back to, or a
working copy you might throw away, both call for a deep copy.

It does cost more, since it rebuilds the whole tree, and `deepcopy` is even smart
enough to handle shared or cyclic references without looping forever. Pick shallow
when a single layer is all you need, and deep when the nesting must be fully
independent.
