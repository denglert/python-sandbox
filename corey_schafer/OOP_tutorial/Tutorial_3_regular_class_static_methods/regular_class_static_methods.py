#!/usr/bin/env python

# - Concepts introduced:
# * regular instance method
# * classmethod
# * staticmethod
# * alternative constructor
# * self
# * cls

class Employee:

    num_of_emps  = 0     # - This is a class variable
    raise_amount = 1.04  # - This is a class variable

    def __init__(self, first, last, pay): # - Constructor method
        self.first = first                # the instance is first argument
        self.last  = last                 # the convention is 'self'
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1         # - You should use the class variable
                                          # here instead of the instance variable 'self'

    def PrintFullName(self):                          # - This is a regular method,
        print('{} {}'.format(self.first, self.last))  # it automatically takes the instance as
                                                      # the first argument

    def PrintDetails(self):                          # - This is a regular method,
        print('{} {}, pay: {}, email: {}'.format(self.first, self.last,
            self.pay, self.email) )  # it automatically takes the instance as
                                                      # the first argument

    def apply_raise(self):                            # - This is a regular method
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod                    # - Adding 'classmethod' decorator
    def set_raise_amt(cls, amount): # 'cls' stands for class
        cls.raise_amount = amount   # This function takes in the class itself
                                    # as the first argument

    @classmethod                    # - Alternative constructor  
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

####################################################
print('### --- Class methods --- ###\n')

# - Create two instances of the class
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# - Print out current value of the raise_amount
print('emp_1.raise_amount', emp_1.raise_amount)
print('emp_2.raise_amount', emp_2.raise_amount)
print('Employee.raise_amount', Employee.raise_amount)


print('')
# - Set raise_amount from the class
Employee.set_raise_amt(1.05)
# - Print out current value of the raise_amount
print('emp_1.raise_amount', emp_1.raise_amount)
print('emp_2.raise_amount', emp_2.raise_amount)
print('Employee.raise_amount', Employee.raise_amount)

print('')
emp_1.set_raise_amt(1.06)
print('emp_1.raise_amount', emp_1.raise_amount)
print('emp_2.raise_amount', emp_2.raise_amount)
print('Employee.raise_amount', Employee.raise_amount)
print('')

####################################################
print('### --- Alternative constructor--- ###\n')

# - Create new class instances by parsing a string
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steven-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
new_emp_1.PrintDetails()

# - This works, but we need to do this for each new class
# - instances.
# - More efficient way to move forward is to define a new class constructor.

new_emp_2 = Employee.from_string( emp_str_2 )
new_emp_2.PrintDetails()

print('')
####################################################
print('### --- Static methods --- ###\n')

# - We are going to create a function that takes in a date and return whether or
# - not it was a workday.
# - We are going to use a staticmethod

import datetime
my_date = datetime.date(2016, 7, 10) # This is a Sunday

print(Employee.is_workday(my_date))
