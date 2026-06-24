---
title: Bytes and Bytearray
exercise: |
  Write `byte_values(data)` that takes a `bytes` object and returns a list of its
  integer values, in order. Iterating a `bytes` object yields ints directly.
check: |
  assert byte_values(b'AB') == [65, 66]
  assert byte_values(b'') == []
  assert byte_values(bytes([1, 2, 3])) == [1, 2, 3]
---

Where `str` holds characters, `bytes` holds raw 8-bit values, each an int from 0
to 255. A bytes literal looks like `b'abc'`. There is one quirk worth knowing:
indexing a `bytes` gives you an int, so `b'abc'[0]` is 97, but slicing gives you
`bytes` back, so `b'abc'[:1]` is `b'a'`.

`bytes` is immutable, just like `str`. Its mutable sibling is `bytearray`, so
`bytearray(b'abc')` lets you change bytes in place. When Python shows a bytes
object, printable ASCII appears as characters and everything else as `\xNN`.

Build bytes straight from numbers with `bytes([65, 66])`, which gives `b'AB'`.
Reach for bytes whenever you handle data that has not been decoded into text yet:
file contents, network packets, image data.
