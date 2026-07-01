---
title: Code Points and Encodings
exercise: |
  Write a function `code_points(text)` that returns a list with the integer code point of
  each character in `text`, in order. Use `ord`. 
  
  (Tip: This can be done with a list comprehension)
check: |
  assert code_points('AB') == [65, 66]
  assert code_points('café') == [99, 97, 102, 233]
  assert code_points('') == []
---

A Python `str` is a sequence of Unicode code points, not bytes. A code point is
the number Unicode assigns to a character, written like U+0041 for 'A'. That
number is the character's identity. How the character gets stored on disk or sent
over a wire is a separate question, answered by an encoding.

An encoding is the rule that turns code points into bytes, and back again. UTF-8
is the one you will use almost always. The two ideas pull apart clearly with a
quick measurement: `len('café')` is 4 because `str` counts characters, but the
same text encoded to UTF-8 is 5 bytes, since the accented letter needs two.

Move between a character and its code point with `ord('A')`, which gives 65, and
`chr(65)`, which gives it back.
