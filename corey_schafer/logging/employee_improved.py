#!/usr/bin/env python

import logging

logger    = logging.getLogger(__name__)
formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('employee_improved.log')

file_handler.setFormatter(formatter)
logger.setLevel(logging.INFO)

logger.addHandler(file_handler)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Wick')
emp_2 = Employee('John', 'Doe')
emp_3 = Employee('William', 'Smith')
