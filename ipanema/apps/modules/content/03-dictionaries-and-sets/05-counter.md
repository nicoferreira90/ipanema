---
title: Counter for Tallies
exercise: |
  Write `top_two(text)` that returns the two most common whitespace-separated
  words as `(word, count)` pairs, most frequent first. Use `collections.Counter`.
check: |
  assert top_two('a b a c b a') == [('a', 3), ('b', 2)]
  assert top_two('hi hi') == [('hi', 2)]
---

`collections.Counter` is a dict built for counting. Feed it any iterable and it
tallies the items for you. `Counter('abracadabra')` reports five `a`s and two
each of `b` and `r`. You can add more with `c.update(['a', 'a'])`, and
`c.most_common(2)` returns the two highest counts already sorted.

Missing keys read as `0` and never raise, so `c['z']` is just `0`. The standout
feature is `most_common(n)`, which returns the `n` highest counts in order. That
is perfect for top words, top errors, or any leaderboard. Counters also add and
subtract like multisets, as in `c1 + c2`. It is one of the quietly most useful
tools in the standard library.
