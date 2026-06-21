---
title: Missing Keys — get & setdefault
exercise: |
  Write `group_by_first(words)` that returns a dict mapping each word's first
  letter to the list of words starting with that letter, keeping their original
  order. Use `setdefault` to grow the lists.
check: |
  assert group_by_first(['ant', 'bee', 'art']) == {'a': ['ant', 'art'], 'b': ['bee']}
  assert group_by_first([]) == {}
---

Reading a missing key with `d[k]` raises `KeyError`. Two methods soften that.

`d.get(k, default)` returns `default` instead of raising, which is great for a
plain lookup such as `count = counts.get(word, 0)`.

`d.setdefault(k, default)` is the one for accumulating. It inserts the default
only if the key is absent, then returns whatever is now stored, so you fetch and
update in a single step. The line `index.setdefault(letter, []).append(word)`
grows a list under each key.

That one line replaces a three-line "if key not in d" dance, and it touches the
dict only once. Use `get` when you just want to read with a fallback, and
`setdefault` when you want to read or create a mutable value and add to it.
