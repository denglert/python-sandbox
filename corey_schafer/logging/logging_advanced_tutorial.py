#!/usr/bin/env python

import logging
import employee_improved

logger    = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('logging_advanced.log')

file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

################

def add(x,y):
    """Add function"""
    return x + y

def subtract(x,y):
    """Subtract function"""
    return x - y 

def multiply(x,y):
    """Multiply function"""
    return x*y

def divide(x,y):
    return x/y


num_1 = 1
num_2 = 5

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result) )

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result) )

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result) )

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result) )
