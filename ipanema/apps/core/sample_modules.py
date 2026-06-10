"""Stand-in module data for the UI prototypes.

Mirrors the shape the future ORM models will expose, so templates can be
reused unchanged once modules live in the database. Chapter titles follow
Luciano Ramalho's *Fluent Python*, 2nd edition.
"""

MODULES = [
    {
        "number": 1,
        "slug": "the-python-data-model",
        "title": "The Python Data Model",
        "part": "Part I — Data Structures",
        "tagline": "Dunder methods & the secret life of objects",
        "blurb": (
            "Why len(x) isn't a method call, how __repr__ earns its keep, "
            "and what makes an object feel Pythonic. The chapter that "
            "reveals the language's master plan."
        ),
        "lessons": [
            "A Pythonic Card Deck",
            "How Special Methods Are Used",
            "Emulating Numeric Types",
            "String Representation",
            "Boolean Value of an Object",
        ],
        "exercise_count": 8,
        "status": "available",
        "color": "coral",
    },
    {
        "number": 2,
        "slug": "an-array-of-sequences",
        "title": "An Array of Sequences",
        "part": "Part I — Data Structures",
        "tagline": "Lists, tuples, slices & the sequence protocol",
        "blurb": (
            "List comprehensions without guilt, tuples as records, the "
            "quiet elegance of slicing, and when a deque beats a list. "
            "Sequences as one unified idea."
        ),
        "lessons": [
            "Overview of Built-In Sequences",
            "List Comprehensions & Genexps",
            "Tuples Are Not Just Immutable Lists",
            "Slicing",
            "When a List Is Not the Answer",
        ],
        "exercise_count": 10,
        "status": "available",
        "color": "teal",
    },
    {
        "number": 3,
        "slug": "dictionaries-and-sets",
        "title": "Dictionaries and Sets",
        "part": "Part I — Data Structures",
        "tagline": "Hash tables, the engine room of Python",
        "blurb": "",
        "lessons": [],
        "exercise_count": 0,
        "status": "coming_soon",
        "color": "yellow",
    },
    {
        "number": 4,
        "slug": "unicode-text-versus-bytes",
        "title": "Unicode Text Versus Bytes",
        "part": "Part I — Data Structures",
        "tagline": "Strings, encodings & the bytes beneath",
        "blurb": "",
        "lessons": [],
        "exercise_count": 0,
        "status": "coming_soon",
        "color": "green",
    },
    {
        "number": 5,
        "slug": "data-class-builders",
        "title": "Data Class Builders",
        "part": "Part I — Data Structures",
        "tagline": "namedtuple, @dataclass & friends",
        "blurb": "",
        "lessons": [],
        "exercise_count": 0,
        "status": "coming_soon",
        "color": "raspberry",
    },
    {
        "number": 6,
        "slug": "object-references-mutability-recycling",
        "title": "Object References, Mutability, and Recycling",
        "part": "Part I — Data Structures",
        "tagline": "Variables are labels, not boxes",
        "blurb": "",
        "lessons": [],
        "exercise_count": 0,
        "status": "coming_soon",
        "color": "aqua",
    },
]

TOTAL_PLANNED = 30
