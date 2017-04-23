#!/usr/bin/env python

# - Employee class

class Employee:
    pass

# - Class variable:    Variables that are shared among all instances of a class
# - Instance variable: Contain data that is unique to each instance

emp_1 = Employee()
emp_2 = Employee()

print('emp_1', emp_1)
print('emp_2', emp_2)

emp_1.first = 'Corey'
emp_1.last  = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay   = 50000

emp_2.first = 'Test'
emp_2.last  = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay   = 60000

print('emp_1.email', emp_1.email)
print('emp_2.email', emp_2.email)

print('### --- End of first segment --- ###\n')

###########################################

class Employee:

    def __init__(self, first, last, pay): # - Constructor method
        self.first = first                # the instance is first argument
        self.last  = last                 # the convention is 'self'
        self.pay   = pay
        self.email = first + '.' + last + 'company.com'

#   def PrintFullName(): # you should always place 'self' as the first argument
#       pass             # which is automatically passed when a class method is
#                        # invoked

    def PrintFullName(self):
        print('{} {}'.format(self.first, self.last))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.PrintFullName()
emp_2.PrintFullName()

print()

emp_1.PrintFullName()           # This does the same thing
Employee.PrintFullName(emp_1)   # as this.

print('### --- End of second segment --- ###\n')
