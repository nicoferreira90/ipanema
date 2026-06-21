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

A `collections.defaultdict` calls a factory to create the value the first time
a key is looked up, so you never check whether it exists. With
`counts = defaultdict(int)`, a missing key starts at `0`, so `counts[word] += 1`
just works inside a loop. With `groups = defaultdict(list)`, a missing key
starts as `[]`, so `groups[word[0]].append(word)` builds lists by first letter.

You pass the callable itself, such as `int`, `list`, or `set`, not a value. The
factory runs only on a genuinely missing key, triggered by `d[k]`. It is the
cleaner cousin of `setdefault` when nearly every access might need a default. A
plain `defaultdict` compares equal to the matching `dict`, so your tests just
work.
