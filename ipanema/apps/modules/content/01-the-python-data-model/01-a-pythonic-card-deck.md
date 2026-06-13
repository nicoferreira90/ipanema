---
title: A Pythonic Card Deck
exercise: |
  Make a class `Shelf` that wraps a list given to `__init__`, so that `len(sh)`
  returns the number of items and `sh[i]` returns the item at that index
  (negative indexes included — let the wrapped list do the work).
check: |
  sh = Shelf(['a', 'b', 'c'])
  assert len(sh) == 3, "len(sh) should use __len__"
  assert sh[0] == 'a', "sh[0] should use __getitem__"
  assert sh[-1] == 'c', "negative indexing should work for free"
---

Python's power comes from a set of **special methods** — the *dunders*
(double-underscore names) the interpreter calls on your behalf.

Implement just two and an object starts behaving like a sequence:

```python
class Deck:
    def __init__(self, cards):
        self._cards = cards
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, i):
        return self._cards[i]
```

Now `len(deck)`, `deck[0]`, slicing, iteration, and `random.choice(deck)` all
just work — because they're built on `__len__` and `__getitem__`. You delegate
to the wrapped list and inherit decades of sequence behaviour. You write two
methods; Python gives you the protocol.
