---
title: An Array of Sequences
part: "Part I: Data Structures"
tagline: Lists, tuples, slices & the sequence protocol
color: teal
status: available
project:
  title: Tournament Standings
  brief: |
    Compute a league table from a season's results with a single function.

    Write a function named `standings(matches)` where `matches` is a list of
    `(home, away, home_goals, away_goals)` tuples. Score each game, where a win
    is worth 3 points, a draw 1, and a loss 0, then total the points per team.

    Return a list of `(team, points)` tuples sorted by points from highest to
    lowest, breaking ties by team name in alphabetical order.

    Use what the chapter covered: unpack each tuple in the `for` loop,
    accumulate the totals in a dict, then sort with `sorted(..., key=...)` and a
    tuple key. Aim for about 15 to 20 lines.
  check: |
    matches = [
        ('A', 'B', 1, 0),
        ('B', 'C', 1, 0),
        ('C', 'A', 1, 0),
        ('A', 'C', 2, 0),
    ]
    table = standings(matches)
    assert table == [('A', 6), ('B', 3), ('C', 3)], table
    assert standings([]) == [], "no matches -> empty table"
    draw = standings([('X', 'Y', 0, 0)])
    assert draw == [('X', 1), ('Y', 1)], draw
---

Seven short lessons on Python's sequences: the workhorses of the language.
Comprehensions, tuple unpacking, slicing, and the sharp edges of `+` and `*`,
then a league table that ties them all together.
