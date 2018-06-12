#!/usr/bin/env python

def basic_generator_function():
    
    yield 1

    yield 2

    yield 3


generator_instance = basic_generator_function()

print(next(generator_instance))
print(next(generator_instance))
print(next(generator_instance))
print(next(generator_instance))

