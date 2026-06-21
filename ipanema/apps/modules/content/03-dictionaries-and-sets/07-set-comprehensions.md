---
title: Set Comprehensions & Hashability
exercise: |
  Write `unique_lengths(words)` that returns the set of the distinct lengths of
  the words. Build it with a set comprehension.
check: |
  assert unique_lengths(['a', 'bb', 'cc', 'ddd']) == {1, 2, 3}
  assert unique_lengths([]) == set()
---

A set comprehension builds a set in one expression, and duplicates collapse
automatically. You can collect the distinct word lengths with
`{len(w) for w in words}`, or the initials with `{name[0] for name in names}`.
It has the same shape as a dict comprehension but with no colon, just the item.

This all works because set members and dict keys must be hashable. Numbers,
strings, and tuples of hashables qualify, while lists and dicts do not, since
their contents can change. Hashability is what lets sets and dicts find an item
in roughly one step instead of scanning, because the hash sends Python almost
straight to the slot. That is the engine room of the chapter: the same
hash-table machinery powers fast membership for sets and fast lookup for dicts.
