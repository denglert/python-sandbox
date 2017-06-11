# Item 3

## Python 3

Two types that represent sequences of characters:
- `bytes`: contains raw 8-bit values
- `str`: contain unicode characters

## Python 2

Two types that represent sequences of characters:
- `str`: contains raw 8-bit values
- `unicode`: contain unicode characters

## Unicode en- and decoding

Unicode characters -> `encode` -> binary data
binary data -> `decode` -> unicode characters

Most common encoding: UTF-8

The unicode types (`str` instances in python 3 and `unicode` instances in python 2) do not have an
associated binary encoding.

What is important:
- to do encoding and decoding of Unicode at the furthest boundary of the interface of the program.
- the core should use Unicode character types, and should not assumen anything about character
  encodings
- this approach allows you to be flexible about alternative text encodings (e.g. Latin-1, Big5,
  etc.), while being strict about your output text encoding (ideally UTF-8)
