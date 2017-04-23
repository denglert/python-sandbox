###############################
### --- Derived classes --- ###
###############################

# - Concepts introduced:
# * inheritance
# * method resolution order
# * chain of inheritance
# * builtins.objects
# * isinstance
# * issubclass

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
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

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)           # - This is more maintainable
#       Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

    def PrintDetails(self):
        super().PrintDetails()
        print('\b{}'.format( self.prog_lang) )


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname() )


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.PrintDetails()
emp_2.PrintDetails()

#####################################################

dev_1 = Developer('John', 'Doe', 80000, 'Python')
dev_2 = Developer('Janet', 'Jackson', 80000, 'Java')

dev_1.PrintDetails()
dev_2.PrintDetails()

# print( help(Developer) )

print( 'dev_1.pay: ', dev_1.pay )
dev_1.apply_raise()
print( 'dev_1.pay: ', dev_1.pay )

#####################################################

mgr_1 = Manager('Hugo', 'Boss', 100000, [dev_1])

mgr_1.PrintDetails()
mgr_1.print_emps()

mgr_1.PrintDetails()
mgr_1.add_emp( emp_1 )
mgr_1.add_emp( emp_2 )
mgr_1.remove_emp( dev_1 )
mgr_1.print_emps()

#######################################################

# - isinstance tells us whether an object is an instance of a class
print('isinstance(mgr_1, Manager):', isinstance(mgr_1, Manager))
print('isinstance(mgr_1, Developer):', isinstance(mgr_1, Developer))

# - issubclass tells us whether an object is a subclass of a class
print('issubclass(Manager, Manager):', issubclass(Manager, Manager))
print('issubclass(Developer, Employee):', issubclass(Developer, Employee))
print('issubclass(Manager, Employee):', issubclass(Manager, Employee))
print('issubclass(Employee, Developer):', issubclass(Employee, Developer))

#######################################################
