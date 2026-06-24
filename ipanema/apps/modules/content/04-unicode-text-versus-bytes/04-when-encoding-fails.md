---
title: When Encoding Fails
exercise: |
  Write `to_ascii(text)` that encodes `text` to ASCII, drops any character ASCII
  cannot represent, and returns the result as a `str` (decode the bytes back).
  Use `errors='ignore'`.
check: |
  assert to_ascii('café') == 'caf'
  assert to_ascii('hello') == 'hello'
  assert to_ascii('Ünïcödé') == 'ncd'
---

Not every encoding can represent every character. Encoding the accented `é` as
ASCII raises `UnicodeEncodeError`, because ASCII simply has no code for it.
Decoding bytes with the wrong encoding raises `UnicodeDecodeError`, or worse,
silently hands you the wrong characters.

Both `encode` and `decode` accept an `errors` argument that decides what happens
on failure. `errors='ignore'` drops the offending characters, while
`errors='replace'` swaps them for a marker, a `?` when encoding and the `�`
character when decoding. So `'café'.encode('ascii', errors='ignore')` gives
`b'caf'`.

Keep the default `'strict'` while you are developing, so problems surface loudly
the moment they happen. Switch to `'ignore'` or `'replace'` only once you have
decided, on purpose, that quietly losing those characters is acceptable.
