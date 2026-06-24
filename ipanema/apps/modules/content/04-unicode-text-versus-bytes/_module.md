---
title: Unicode Text Versus Bytes
part: "Part I: Data Structures"
tagline: Strings, encodings & the bytes beneath
color: green
status: available
project:
  title: URL Slugs
  placeholder: "# write your slugify function here"
  brief: |
    Turn any title into the kind of clean slug you see in a web address:
    lowercase ASCII, words joined by single hyphens, accents stripped away.

    Write a function named `slugify(text)` that does the following, in order:

    - Strip accents by normalizing with NFKD, then dropping every character for
      which `unicodedata.combining(ch)` is nonzero.
    - Force plain ASCII with an encode and decode round trip, like
      `text.encode('ascii', errors='ignore').decode('ascii')`.
    - Lowercase everything.
    - Collapse every run of non-alphanumeric characters into a single hyphen. A
      small regex like `re.sub(r'[^a-z0-9]+', '-', s)` is the easy way.
    - Remove any leading or trailing hyphen.

    This pulls the whole chapter together: normalization to separate accents from
    letters, the Unicode database to spot the combining marks, and an encode and
    decode round trip to drop anything that is not ASCII. Aim for about 12 to 18
    lines.
  check: |
    assert slugify('Café Crème') == 'cafe-creme'
    assert slugify('Hello, World!') == 'hello-world'
    assert slugify('  Niño  ') == 'nino'
    assert slugify('ÀÉÎÕÜ') == 'aeiou'
    assert slugify('a--b__c') == 'a-b-c'
---

Six short lessons on the line between text and bytes. Code points, encodings, the
bytes type, the errors that bite when they meet, the Unicode sandwich for safe
text I/O, and normalizing so comparisons behave, then a slugifier that ties them
all together.
