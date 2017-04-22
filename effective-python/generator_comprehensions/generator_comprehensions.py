#!/usr/bin/env python

# - List comprehension

value = [ len(x) for x in open('test_file.txt') ]
print(value)

# - Generator expression

it = (len(x) for x in open('test_file.txt'))

print(it)
print(next(it))
print(next(it))
print(next(it))

# - Chaining generators together

roots = ((x, x**0.5) for x in it)

print(next(roots))
print(next(roots))
print(next(roots))
