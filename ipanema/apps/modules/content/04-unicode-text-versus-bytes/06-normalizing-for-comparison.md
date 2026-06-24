---
title: Normalizing for Comparison
exercise: |
  Write `same_text(a, b)` that returns `True` when `a` and `b` are equal after
  NFC normalization, even if they were typed with different code point forms.
  Use `unicodedata.normalize`.
check: |
  import unicodedata
  nfd = unicodedata.normalize('NFD', 'café')
  assert same_text('café', nfd) is True
  assert same_text('café', 'cafe') is False
  assert same_text('abc', 'abc') is True
---

The same text can hide two different code point sequences. The word `café` might
store its accented `é` as a single code point, or as a plain `e` followed by a
separate combining accent. The two look identical on screen, yet `==` reports
them as different and even `len` disagrees.

`unicodedata.normalize` settles this by rewriting text into a canonical form. NFC
composes characters into their shortest form, while NFD decomposes them, splitting
that accent back out as a combining mark you can detect with
`unicodedata.combining`. Normalize both sides to the same form before comparing,
as in `normalize('NFC', a) == normalize('NFC', b)`.

For case-insensitive matching, reach for `str.casefold`, the Unicode-aware cousin
of `lower` that even handles tricky cases like German `ß`. Comparing text a user
typed without normalizing first is a bug waiting to happen.
