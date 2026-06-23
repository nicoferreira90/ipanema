---
title: Slicing
exercise: |
  Write a function named `every_other(seq)` that returns every item at an even index, so
  positions 0, 2, 4, and so on. A single slice does it, and the same code
  should work for both lists and strings.
check: |
  assert every_other([0, 1, 2, 3, 4, 5]) == [0, 2, 4]
  assert every_other('abcdef') == 'ace'
  assert every_other([]) == []
---

Slicing reads a range of a sequence with `seq[start:stop:step]`. Any part can
be left out, `stop` is excluded, and negatives count from the end. For
`s = 'bicycle'`, `s[2:5]` is `'cyc'`, `s[::2]` takes every other letter to give
`'bcce'`, and `s[::-1]` reverses it to `'elcycib'`.

A slice always returns a new object of the same type, so slicing a list gives a
list and a string gives a string. On a mutable sequence you can even assign to a
slice to splice items in or out, as in `nums[1:3] = [9]`. Slicing beats a
hand-written index loop, because it is shorter, it is faster, and the intent is
obvious at a glance.
