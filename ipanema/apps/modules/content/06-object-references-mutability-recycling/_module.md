---
title: Object References, Mutability, and Recycling
part: "Part I: Data Structures"
tagline: Variables are labels, not boxes
color: aqua
status: available
project:
  title: Undo History
  placeholder: "# build your History class here"
  brief: |
    Build a small editor that can undo. The trick is references: if you save the
    live list itself, every snapshot is just another label for the same object and
    they all change together. The fix is a deep copy.

    Write a class named `History` that tracks one mutable document, a list of
    strings called `lines`.

    - `History(lines)` stores the starting lines.
    - `add(line)` appends a line to the current document.
    - `snapshot()` saves the current state so you can return to it. Save a
      `copy.deepcopy` of `lines`, not the list itself, or every snapshot would
      alias the live document.
    - `undo()` restores `lines` to the most recent snapshot and drops that
      snapshot. With no snapshot saved, leave `lines` unchanged.

    Keep the saved states in a list used as a stack. Aim for about 15 to 20 lines.
  check: |
    import copy
    h = History(['a'])
    h.snapshot()
    h.add('b')
    assert h.lines == ['a', 'b']
    h.undo()
    assert h.lines == ['a']
    h.undo()
    assert h.lines == ['a']
    h2 = History(['x'])
    h2.snapshot()
    h2.lines.append('y')
    assert h2.lines == ['x', 'y']
    h2.undo()
    assert h2.lines == ['x']
---

Six short lessons on what a variable really is. Names as labels, the gap between
identity and equality, how aliases share changes, shallow versus deep copies, and
why a tuple can hold something that still changes, then an undo stack that depends
on getting copies right.
