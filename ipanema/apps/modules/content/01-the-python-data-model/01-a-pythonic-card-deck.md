---
title: A Pythonic Card Deck
exercise: |
  Make a class `Shelf` that wraps a list passed to `__init__`. Make `len(sh)`
  return how many items it holds, and `sh[i]` return the item at index `i`.
  Let the wrapped list do the indexing, so negative indexes work too.
check: |
  sh = Shelf(['a', 'b', 'c'])
  assert len(sh) == 3, "len(sh) should use __len__"
  assert sh[0] == 'a', "sh[0] should use __getitem__"
  assert sh[-1] == 'c', "negative indexing should work for free"
---

Python's power comes from a set of special methods, the dunders (the
double-underscore names) that the interpreter calls on your behalf.

Implement just two and an object starts behaving like a sequence. Give a class
a `__len__` that returns `len(self._cards)` and a `__getitem__` that returns
`self._cards[i]`, with both delegating to a wrapped list.

Now `len(deck)`, `deck[0]`, slicing, iteration, and `random.choice(deck)` all
just work, because they build on `__len__` and `__getitem__`. You delegate to
the wrapped list and inherit decades of sequence behaviour. You write two
methods, and Python gives you the protocol.
