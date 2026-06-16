---
title: Slicing
exercise: |
  Write `every_other(seq)` that returns every item at an even index (0, 2,
  4, …). One slice does it — and it should work for both lists and strings.
check: |
  assert every_other([0, 1, 2, 3, 4, 5]) == [0, 2, 4]
  assert every_other('abcdef') == 'ace'
  assert every_other([]) == []
---

Slicing reads a *range* of a sequence with `seq[start:stop:step]`. Any part can
be left out, `stop` is excluded, and negatives count from the end:

```python
s = 'bicycle'
s[2:5]      # 'cyc'
s[::2]      # 'bcce'    (every other)
s[::-1]     # 'elcycib' (reversed)
```

A slice always returns a **new** object of the same type — slicing a list gives
a list, a string gives a string. On a mutable sequence you can even assign to a
slice to splice items in or out: `nums[1:3] = [9]`. Slicing beats a hand-written
index loop: it's shorter, it's faster, and the intent is obvious at a glance.
