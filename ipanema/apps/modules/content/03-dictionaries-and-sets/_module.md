---
title: Dictionaries and Sets
part: Part I — Data Structures
tagline: Hash tables, the engine room of Python
color: yellow
status: available
project:
  title: Inverted Index
  brief: |
    Build the data structure behind every search engine. An **inverted index**
    maps each word to the documents it appears in.

    Write `build_index(docs)` where `docs` is a list of `(doc_id, text)`
    tuples. Split each `text` on whitespace, lowercase every word, and record
    which documents contain it.

    Return a dict mapping each word to a **sorted list** of the distinct
    `doc_id`s that contain it.

    Use the chapter: `setdefault` (or a `defaultdict`) to grow the entries, a
    **set** to dedupe the ids, and a dict comprehension to finish. ~12–18 lines.
  check: |
    docs = [
        (1, 'the cat sat'),
        (2, 'the dog sat'),
        (3, 'the CAT ran'),
    ]
    idx = build_index(docs)
    assert idx['the'] == [1, 2, 3], idx
    assert idx['cat'] == [1, 3], "case-folded and deduped"
    assert idx['sat'] == [1, 2], idx
    assert idx['ran'] == [3], idx
    assert 'CAT' not in idx, "words are lowercased"
---

Seven short lessons on Python's mappings and sets — the hash-table machinery the
whole language leans on. Comprehensions, smart defaults, `Counter`, and set
algebra, then an inverted index that puts them to work.
