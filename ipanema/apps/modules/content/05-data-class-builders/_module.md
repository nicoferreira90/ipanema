---
title: Data Class Builders
part: "Part I: Data Structures"
tagline: namedtuple, @dataclass & friends
color: raspberry
status: available
project:
  title: Order Total
  placeholder: "# build your LineItem and Order classes here"
  brief: |
    Build a tiny order system from two dataclasses, the kind of thing behind any
    checkout page.

    First, a `LineItem` with three fields: `name` (a `str`), `quantity` (an
    `int`), and `unit_price` (a `float`). Give it a `subtotal` that returns
    `quantity * unit_price`. Make `subtotal` a `property` so it reads like a field
    but is computed on the fly: write `@property` on the line above a method that
    returns `self.quantity * self.unit_price`.

    Then an `Order` with a single field `cart` that starts as an empty list. Use
    `field(default_factory=list)` so separate orders never share one cart. Give
    `Order` two methods: `add(item)` appends a `LineItem` to the cart, and
    `total()` returns the sum of every line's `subtotal`.

    Use `@dataclass` for both classes. Aim for about 15 to 20 lines.
  check: |
    order = Order()
    order.add(LineItem('apple', 3, 0.5))
    order.add(LineItem('bread', 2, 1.25))
    assert order.cart[0].subtotal == 1.5
    assert order.total() == 4.0
    empty = Order()
    assert empty.total() == 0
    assert empty.cart == []
---

Six short lessons on letting Python write your boilerplate. The classic namedtuple
and its tuple superpowers, the typed NamedTuple, why type hints are never enforced,
and the flexible @dataclass, then an order total that puts them to work.
