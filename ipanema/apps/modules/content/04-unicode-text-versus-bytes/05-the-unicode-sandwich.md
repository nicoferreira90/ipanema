---
title: The Unicode Sandwich
exercise: |
  Write `decoded_lines(data)` that takes a `bytes` object holding UTF-8 text with
  newline-separated lines and returns a list of the decoded lines, with no
  trailing newline characters. Decode first, then use `splitlines`.
check: |
  assert decoded_lines(b'a\nb\nc') == ['a', 'b', 'c']
  assert decoded_lines('café\nnoir'.encode()) == ['café', 'noir']
  assert decoded_lines(b'') == []
---

The reliable way to handle text is the Unicode sandwich. Decode bytes to `str`
as early as possible, do all of your work on `str`, and encode back to bytes only
at the very end. The middle of your program should never touch raw bytes.

`open()` does the decoding and encoding for you, but only if you tell it which
encoding to use, as in `open(path, encoding='utf-8')`. Never lean on the default,
which changes from one machine to the next and is the classic source of the
"works on my laptop" bug.

Read hands you `str`, write takes `str`, and the bytes stay out at the edges
where they belong. It comes down to one habit worth keeping for good: always pass
`encoding=` when you call `open`.
