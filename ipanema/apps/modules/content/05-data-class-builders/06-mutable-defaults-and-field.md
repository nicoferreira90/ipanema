---
title: Mutable Defaults and field()
exercise: |
  Use `@dataclass` to define a class `Basket` with one field `items` that
  defaults to a new empty list, using `field(default_factory=list)`. Two baskets
  must not share the same list. Import `dataclass` and `field` from `dataclasses`.
check: |
  b1 = Basket()
  b2 = Basket()
  b1.items.append('egg')
  assert b1.items == ['egg']
  assert b2.items == []
---

Giving a dataclass field a default looks easy, as in `count: int = 0`. But a
mutable default like `tags: list = []` is a trap. That one list would be shared by
every instance that uses the default, so appending to one would secretly change
them all. Python actually refuses this and raises an error to protect you.

The fix is `field` from `dataclasses`. Pass it a `default_factory`, a callable
that builds a fresh value for each new instance, as in
`tags: list = field(default_factory=list)`. Now every instance starts with its
own empty list.

`field` does more than defaults. The factory is the common case, but `field` can
also control whether an attribute joins the repr or the comparison. And if you
want the whole class immutable like a namedtuple, decorate with
`@dataclass(frozen=True)`.
