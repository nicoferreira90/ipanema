---
title: Sorting, Keys & When a List Isn't the Answer
exercise: |
  Write `by_length(words)` that returns the words sorted by length (shortest
  first), breaking ties alphabetically. Use `sorted` with a `key` — and don't
  mutate the input.
check: |
  assert by_length(['bb', 'a', 'ccc', 'aa']) == ['a', 'aa', 'bb', 'ccc']
  assert by_length([]) == []
---

`list.sort()` orders a list **in place** and returns `None`; the `sorted()`
built-in leaves its argument untouched and returns a **new** list — so it works
on any iterable. Both take a `key` function applied to each item to decide the
order, plus `reverse=True`:

```python
sorted(words, key=len)
sorted(words, key=lambda w: (len(w), w))   # length, then alphabetical
```

A tuple key sorts by the first field, then the next — perfect for tie-breaks.

A list isn't always the right container. For millions of numbers an
`array.array` is leaner; for fast appends and pops at *both* ends, a
`collections.deque`. Pick the structure that fits the access pattern — the list
is the default, not the only choice.
