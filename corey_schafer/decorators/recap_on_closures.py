#!/usr/bin/env python

#########################
# - Recap on closures - #
#########################

def outer_function():
    message = 'Hi'    # - local variable

    def inner_function():
        print(message)
    return inner_function()

outer_function()

#############################

def outer_function():
    message = 'Hi'    # - local variable

    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()

my_func()

#############################

def outer_function(msg):
    message = msg    # - local variable

    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

###############################
# - Cutting out the middle man

def outer_function(msg):

    def inner_function():
        print(msg)
    return inner_function

hello_func = outer_function('Hello')
ciao_func = outer_function('Ciao')

hello_func()
ciao_func()
