---
title: Building Sequences with + and *
exercise: |
  Write `zeros(n)` that returns an `n`×`n` grid: a list of `n` rows, each a list
  of `n` zeros. Each row must be independent — changing one cell must not change
  another row's.
check: |
  g = zeros(3)
  assert g == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  g[0][0] = 5
  assert g[1][0] == 0, "rows must not share the same list"
---

`+` and `*` build new sequences without touching their operands:

```python
[1, 2] + [3]        # [1, 2, 3]
[0] * 4             # [0, 0, 0, 0]
'ab' * 3            # 'ababab'
```

But there's a classic trap. `[[0] * 3] * 3` looks like a 3×3 grid — yet it holds
the **same inner list three times**, so setting `grid[0][0]` changes every row.
The `*` copied the *reference*, not the list. Build the rows independently with
a comprehension instead:

```python
grid = [[0] * 3 for _ in range(3)]
```

Rule of thumb: `*` is safe for immutable items (numbers, strings); when the item
is mutable and you want distinct copies, reach for a comprehension.
