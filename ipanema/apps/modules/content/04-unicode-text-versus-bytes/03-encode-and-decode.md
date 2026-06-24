---
title: Encode and Decode
exercise: |
  Write `roundtrip(text, encoding)` that encodes `text` with `encoding`, decodes
  the bytes back with the same `encoding`, and returns the result. It should
  equal the original `text`.
check: |
  assert roundtrip('café', 'utf-8') == 'café'
  assert roundtrip('hello', 'ascii') == 'hello'
  assert roundtrip('niño', 'latin-1') == 'niño'
---

Two methods bridge the gap between text and bytes. `str.encode(encoding)` turns
characters into bytes, and `bytes.decode(encoding)` turns bytes back into
characters. They are inverses as long as you use the same encoding both ways. So
`'café'.encode('utf-8')` gives `b'caf\xc3\xa9'`, and calling `.decode('utf-8')`
on that returns `'café'`.

UTF-8 is the default and the right choice almost always, so `'café'.encode()`
already means UTF-8 without you spelling it out.

Different encodings produce different bytes for the same text: the accented `é`
is two bytes in UTF-8 but a single byte in latin-1. That leads to the golden
rule of this chapter. Always know which encoding you are using, and decode with
the same one you encoded with. Mixing them is how readable text turns to garbage.
