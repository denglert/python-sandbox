#!/usr/bin/env python

class Employee:

    num_of_emps  = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): # - Constructor method
        self.first = first                # the instance is first argument
        self.last  = last                 # the convention is 'self'
        self.pay   = pay
        self.email = first + '.' + last + 'company.com'
        Employee.num_of_emps += 1         # - You should use the class variable
                                          # here instead of the instance variable 'self'

    def PrintFullName(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) # this is a global 
#        self.pay = int(self.pay * self.raise_amount) # this is local is not the
#                                                     # same as the # previous line !!!  print('')

print('Employee.num_of_emps', Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print('Employee.num_of_emps', Employee.num_of_emps)

print('emp_1.pay', emp_1.pay)
emp_1.apply_raise()
print('emp_1.pay', emp_1.pay)

print('### --- End of first segment --- ###\n')
#################################################

print('emp_1.raise_amount', emp_1.raise_amount)
print('emp_2.raise_amount', emp_2.raise_amount)
print('Employee.raise_amount', Employee.raise_amount)

print('### --- End of second segment --- ###\n')
#################################################

print('emp_1.__dict__',    emp_1.__dict__)
print('')
print('Employee.__dict__', Employee.__dict__)

print('### --- End of third segment --- ###\n')
#################################################

print('Setting the Employee.raise_amount to 1.05.')
Employee.raise_amount = 1.05

print('emp_1.raise_amount', emp_1.raise_amount)
print('emp_2.raise_amount', emp_2.raise_amount)
print('Employee.raise_amount', Employee.raise_amount)
print('emp_1.__dict__',    emp_1.__dict__)

print()

print('Setting the emp_1.raise_amount to 1.07.')
emp_1.raise_amount = 1.07
print('emp_1.raise_amount', emp_1.raise_amount)
print('emp_2.raise_amount', emp_2.raise_amount)
print('Employee.raise_amount', Employee.raise_amount)
print('emp_1.__dict__',    emp_1.__dict__)


print('### --- End of fourth segment --- ###\n')

#################################################

print('Employee.num_of_emps', Employee.num_of_emps)
print('### --- End of fifth segment --- ###\n')
