##################################################################
### --- Property decorators: Getters, setters and deleters --- ###
##################################################################

# - Concepts introduced:
# * propery decorator
# * class attributes:
# * getters
# * setters
# * deleters

class Employee:

    def __init__(self, first, last ):
        self.first = first               
        self.last  = last                
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print('emp_1.first:', emp_1.first)
print('emp_1.email:', emp_1.email)
print('emp_1.fullname():', emp_1.fullname())
print()

# - Now let's say we need to change the first name
emp_1.first = 'Jim'

# - Unfortunately this doesn't change the e-mail address accordingly

print('emp_1.first:', emp_1.first)
print('emp_1.email:', emp_1.email)
print('emp_1.fullname():', emp_1.fullname())
print()

# - We need to update the e-mail address somehow
# - Possible solutions:
# * write an e-mail method

print('####################\n')

class Employee:

    def __init__(self, first, last ):
        self.first = first               
        self.last  = last                
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
 

emp_1 = Employee('John', 'Smith')

print('emp_1.first:',      emp_1.first      )
print('emp_1.fullname():', emp_1.fullname() )
print('emp_1.email():',    emp_1.email()    )
print()

emp_1.first = 'Jim'

print('emp_1.first:', emp_1.first)
print('emp_1.email:', emp_1.email())
print('emp_1.fullname():', emp_1.fullname())
print()


print('####################\n')

class Employee:

    def __init__(self, first, last ):
        self.first = first               
        self.last  = last                
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
 

emp_1 = Employee('John', 'Smith')

print('emp_1.first:',      emp_1.first      )
print('emp_1.fullname:',   emp_1.fullname   )
print('emp_1.email:',      emp_1.email      )
print()

emp_1.first = 'Jim'

print('emp_1.first:', emp_1.first)
print('emp_1.email:', emp_1.email)
print('emp_1.fullnam):', emp_1.fullname)
print()

# - This doesn't work.
#emp_1.fullname = 'Corey Schafer'

print('####################\n')

class Employee:

    def __init__(self, first, last ):
        self.first = first               
        self.last  = last                
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last  = last

    @fullname.deleter
    def fullname(self):
        print('Name deleted.')
        self.first = None
        self.last  = None


emp_1 = Employee('John', 'Smith')

print('emp_1.first:',      emp_1.first      )
print('emp_1.fullname:',   emp_1.fullname   )
print('emp_1.email:',      emp_1.email      )
print()

emp_1.fullname = 'Corey Schafer'

print('emp_1.first:',      emp_1.first      )
print('emp_1.fullname:',   emp_1.fullname   )
print('emp_1.email:',      emp_1.email      )
print()

del emp_1.fullname

print('emp_1.first:',      emp_1.first      )
print('emp_1.fullname:',   emp_1.fullname   )
print('emp_1.email:',      emp_1.email      )
print()
