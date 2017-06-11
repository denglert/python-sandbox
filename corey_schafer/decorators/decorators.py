#!/usr/bin/env python

##########################
### --- Decorators --- ###
##########################

# - Decorator: is a function which takes another function as an argument, adds
# some kind of functionality and then returns another function, all of this
# without altering the source code of the original function which was passed in.

# - Identical to the example in the recap_on_closures.py
def decorator_function(message):

    def wrapper_function():  # Wrapper function within the main decorator func.
        print(message)

    return wrapper_function

########################################

# - Let's pass a function as an argument instead
# - (really basic decorator example)

# - Our original function
def display():
    print ('display function ran.')

# - Decorator function
def decorator_function( original_function ):

    def wrapper_function():
        return original_function() # just return the output of the original
                                   # function
    return wrapper_function


decorated_display = decorator_function(display)

decorated_display()

print('### End of first segment. ###\n')
###########################################

# - Let us add some more functionality to the wrapper

# - Our original function
def display():
    print ('display function ran.')

# - Decorator function
def decorator_function( original_function ):

    def wrapper_function():
        print('wrapper executed this before {}.'.format(
            original_function.__name__ ))
        return original_function() # just return the output of the original
                                   # function
    return wrapper_function


decorated_display = decorator_function(display)
decorated_display()

print('### End of second segment. ###\n')
###########################################

# Using the default syntax for decorators

####################################
# @decorator_function
# def decorated_function_instance():
#   print('display function ran.')
####################################
#
#   is equal to
#
##########################################
# def original_function_definition():
#   print('display function ran.')
#
# decorated_function_instance = decorator_function( original_function_definition )
##############################################


@decorator_function
def decorated_display():
        print('display function ran.')

decorated_display()

print('### End of third segment. ###\n')

##############################################

# - If the original function takes in some arguments

#@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age) )

display_info('John', 25)
print('')

# - What if I would want to decorate this function?
# i.e. 
# @decorator_function
# def display_info(name, age):
#   print('display_info ran with arguments ({}, {})'.format(name, age) )
#
# - This doesn't work.

# - We need to be able to pass any number of positional or keyword arguments
#   to our wrapper, and have it execute our original function with those
#   arguments.

# - Decorator function
def decorator_function( original_function ):

    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}.'.format(
            original_function.__name__ ))
        return original_function(*args, **kwargs) # just return the output of the original
                                   # function
    return wrapper_function

@decorator_function
def display():
        print('display function ran.')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age) )


display()
print('')
display_info('John', 25)

print('### End of fourth segment. ###\n')


##############################################

# - Classes as decorators instead of using functions as decorators

class decorator_class( object ):
    def __init__ (self, original_function): # passing the original function to decorator_class
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('The call method executed this before {}.'.format(
            self.original_function.__name__ ))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('display function ran')


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age) )

display()
print('')
display_info('John', 25)

print('### End of fifth segment. ###\n')


##############################################
# - Practical examples:
#   Example 1: Logging

# - Decorator function
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),
            level=logging.INFO )

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age) )

display_info('Hank', 30)

print('### End of sixth segment. ###\n')
####################
#   Example 2: Timer

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        dt = t2 - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, dt) )
        return result

    return wrapper


import time

@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age) )

display_info('Hank', 30)

print('### End of seventh segment. ###\n')

###############################################

# - Applying multiple decorators to a function

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),
            level=logging.INFO )

    def wrapper(*args, **kwargs):
        logging.info(
            'Hihi Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age) )


display_info1 =  my_timer(display_info)
display_info2 = my_logger(display_info1)

display_info2('Rachel', 19)

#display_info('Hank', 30)
print('display_info.__name__: ',  display_info.__name__)
print('display_info1.__name__: ', display_info1.__name__)
print('display_info2.__name__: ', display_info2.__name__)

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age) )


print('display_info.__name__: ',  display_info.__name__)

display_info('Johny', 28)


print('### End of eight segment. ###\n')
