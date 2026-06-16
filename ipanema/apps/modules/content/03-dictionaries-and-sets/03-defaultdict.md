---
title: defaultdict
exercise: |
  Write `tally(items)` that counts how many times each item appears and returns
  the counts. Use a `collections.defaultdict(int)`.
check: |
  assert tally(['a', 'b', 'a']) == {'a': 2, 'b': 1}
  assert tally([]) == {}
  assert tally(['x']) == {'x': 1}
---

A `collections.defaultdict` calls a factory to create the value the **first
time** a key is looked up, so you never check whether it exists:

```python
from collections import defaultdict

counts = defaultdict(int)        # missing key -> int() -> 0
for word in words:
    counts[word] += 1

groups = defaultdict(list)       # missing key -> []
for word in words:
    groups[word[0]].append(word)
```

You pass the *callable* itself — `int`, `list`, `set` — not a value. The factory
runs only on a genuinely missing key, triggered by `d[k]`. It's the cleaner
cousin of `setdefault` when nearly every access might need a default. (A plain
`defaultdict` compares equal to the matching `dict`, so your tests just work.)
