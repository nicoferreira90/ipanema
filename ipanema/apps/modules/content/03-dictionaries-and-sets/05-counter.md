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
tallies the items for you:

```python
from collections import Counter

c = Counter('abracadabra')      # {'a': 5, 'b': 2, 'r': 2, ...}
c.update(['a', 'a'])            # add more
c.most_common(2)               # [('a', 7), ('b', 2)]
```

Missing keys read as `0`, never raising, so `c['z']` is just `0`. The star
feature is `most_common(n)`, which returns the `n` highest counts already sorted
— perfect for "top words", "top errors", or any leaderboard. Counters also add
and subtract like multisets (`c1 + c2`). It's one of the quietly most useful
tools in the standard library.
