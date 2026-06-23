---
title: Sorting, Keys & When a List Isn't the Answer
exercise: |
  Write a function named `by_length(words)` that returns the words sorted by length, shortest
  first, with ties broken alphabetically. Use `sorted` with a `key`, and do not
  mutate the input.
check: |
  assert by_length(['bb', 'a', 'ccc', 'aa']) == ['a', 'aa', 'bb', 'ccc']
  assert by_length([]) == []
---

`list.sort()` orders a list in place and returns `None`. The `sorted()`
built-in leaves its argument untouched and returns a new list, so it works on
any iterable. Both take a `key` function applied to each item to decide the
order, plus an optional `reverse=True`. You can sort by length with
`sorted(words, key=len)`, or by length and then alphabetically with
`sorted(words, key=lambda w: (len(w), w))`.

A tuple key sorts by the first field, then the next, which is perfect for
tie-breaks.

A list is not always the right container. For millions of numbers an
`array.array` is leaner, and for fast appends and pops at both ends there is
`collections.deque`. Pick the structure that fits the access pattern. The list
is the default, not the only choice.
