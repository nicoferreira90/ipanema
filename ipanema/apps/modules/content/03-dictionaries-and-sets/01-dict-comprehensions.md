---
title: Dict Comprehensions
exercise: |
  Write `to_dict(keys, values)` that pairs each key with the value at the same
  position and returns a dict. Build it with a dict comprehension over `zip`.
check: |
  assert to_dict(['a', 'b'], [1, 2]) == {'a': 1, 'b': 2}
  assert to_dict([], []) == {}
  assert to_dict(['x'], [9]) == {'x': 9}
---

A **dict comprehension** builds a dict from any iterable of key–value pairs, the
same way a listcomp builds a list:

```python
pairs = [('a', 1), ('b', 2)]
d = {k: v for k, v in pairs}
```

`zip` makes the pairs when your keys and values live in separate sequences:

```python
{name: code for name, code in zip(names, codes)}
```

You can transform or filter as you go — flip keys and values with
`{v: k for k, v in d.items()}`, or keep only some entries with an `if`. Modern
dicts also merge with `|` (`a | b`) and unpack with `**` (`{**a, **b}`) — both
produce a new dict, leaving the originals untouched.
