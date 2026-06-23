---
title: Building Sequences with + and *
exercise: |
  Write a function named `zeros(n)` that returns an `n` by `n` grid: a list of `n` rows, where
  each row is a list of `n` zeros. The rows must be independent, so changing one
  cell does not change any other row.
check: |
  g = zeros(3)
  assert g == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  g[0][0] = 5
  assert g[1][0] == 0, "rows must not share the same list"
---

The `+` and `*` operators build new sequences without touching their operands.
So `[1, 2] + [3]` gives `[1, 2, 3]`, `[0] * 4` gives `[0, 0, 0, 0]`, and
`'ab' * 3` gives `'ababab'`.

But there is a classic trap. `[[0] * 3] * 3` looks like a 3 by 3 grid, yet it
holds the same inner list three times, so setting `grid[0][0]` changes every
row. The `*` copied the reference, not the list. Build the rows independently
with a comprehension instead, as in `[[0] * 3 for _ in range(3)]`.

The rule of thumb: `*` is safe for immutable items such as numbers and strings.
When the item is mutable and you want distinct copies, reach for a
comprehension.
