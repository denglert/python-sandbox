##############################################
### --- Special (Magic/Dunder) methods --- ###
##############################################

# - Concepts introduced:
# * special methods
# * operator overloading
# * __*__ = dunder

class Employee:

    raise_amount = 1.04 
    def __init__(self, first, last, pay): # __init__ = dunder init
        self.first = first               
        self.last  = last                
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def PrintFullName(self):                          
        print('{} {}'.format(self.first, self.last))  

    def PrintDetails(self):
        print('{} {}, pay: {}, email: {}'.format(self.first, self.last,
            self.pay, self.email) ) 

#    def __repr__(self): # - Meant for developers
#        pass
#
#    def __str__(self):  # - Meant for the users
#        pass
 

emp_1 = Employee('Corey', 'Schafer', 50000)

# - The '+' operator has different behaviour for different objects
# - E.g. see the result of the following:

print(1+2)
print('a' + 'b')

###############################################################

# - If you only have __repr__, but not no __str__, then __repr__ will be used
# - for str too

print()
print('emp_1', emp_1)

print('repr(emp_1)', repr(emp_1) )
print('str(emp_1)', str(emp_1)  )


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay): # __init__ = dunder init
        self.first = first               
        self.last  = last                
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def PrintFullName(self):                          
        print('{} {}'.format(self.first, self.last))  

    def PrintDetails(self):
        print('{} {}, pay: {}, email: {}'.format(self.first, self.last,
            self.pay, self.email) ) 

    def __repr__(self): # - Meant for developers
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                self.pay)

#    def __str__(self):  # - Meant for the users
#        pass


print()
emp_2 = Employee('Test', 'Employee', 60000)

print('emp_2', emp_2)

print('repr(emp_2)', repr(emp_2) )
print('str(emp_2)', str(emp_2)  )

###############################################################

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay): # __init__ = dunder init
        self.first = first               
        self.last  = last                
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def PrintFullName(self):                          
        print('{} {}'.format(self.first, self.last))  

    def PrintDetails(self):
        print('{} {}, pay: {}, email: {}'.format(self.first, self.last,
            self.pay, self.email) ) 

    def __repr__(self): # - Meant for developers
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                self.pay)

    def __str__(self):  # - Meant for the users
        return '{} - {}'.format(self.fullname(), self.email)


print()
emp_3 = Employee('Wicked', 'Witch', 60000)

print('emp_3', emp_3)

print('repr(emp_3)', repr(emp_3) )
print('str(emp_3)', str(emp_3)  )


###############################################################
# - Arithmetic dunder methods

# - Example: '+'

print('1+2: ', 1+2 )
print('int.__add__(1, 2)', int.__add__(1, 2) )
print("str.__add__('a', 'b')", str.__add__('a', 'b') )


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay): # __init__ = dunder init
        self.first = first               
        self.last  = last                
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def PrintFullName(self):                          
        print('{} {}'.format(self.first, self.last))  

    def PrintDetails(self):
        print('{} {}, pay: {}, email: {}'.format(self.first, self.last,
            self.pay, self.email) ) 

    def __repr__(self): # - Meant for developers
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                self.pay)

    def __str__(self):  # - Meant for the users
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print('emp_1 + emp_2', emp_1 + emp_2)


###############################################################
print()

print("len('test)", len('test') )
print( 'test'.__len__() )


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay): # __init__ = dunder init
        self.first = first               
        self.last  = last                
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def PrintFullName(self):                          
        print('{} {}'.format(self.first, self.last))  

    def PrintDetails(self):
        print('{} {}, pay: {}, email: {}'.format(self.first, self.last,
            self.pay, self.email) ) 

    def __repr__(self): # - Meant for developers
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                self.pay)

    def __str__(self):  # - Meant for the users
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len( self.fullname() )



print()
emp_1 = Employee('Corey', 'Schafer', 50000)

print('len(emp_1)', len(emp_1))

########################################################

# - Examples for datetime module..
