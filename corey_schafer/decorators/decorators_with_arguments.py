#!/usr/bin/env python

# - Example illustrating a decorator with an argument.

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed after', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING:')
def display_info(name, age):
    print('display_info ran with argument ({} {})'.format(name, age))


display_info('John',   25)
display_info('Travis', 30)
