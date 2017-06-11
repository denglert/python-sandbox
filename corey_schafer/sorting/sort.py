# - Original list 
lst = [9,1,8,2,7,3,6,4,5]

print('Original list:\t', lst )

# - Sort list with sorted() function
s_lst = sorted(lst)

print('Sorted list: {0}'.format(s_lst) )

# - Sort lits Using subfunction .sort()

lst.sort()

print('Sorted list:\t', lst )

# - Sort list in reverse order with sorted() function
s_lst = sorted(lst, reverse=True)

print('Sorted list:\t', s_lst )

# - Sort list in reverse order with .sort() subfunction
lst.sort(reverse=True)

print('Sorted list:\t', lst )

#########################

# The sorted() function has more flexibility
# You can also apply it to tuples and dictionaries
# sorted(): tuple      -> list
# sorted(): dictionary -> list of keys

# - Original tuple
tup = (9,1,8,2,7,3,6,4,5)

print('Original tuple:\t', tup )

# - Sort tuple into a list
s_tup = sorted( tup )
print('Sorted tuple:\t', s_tup )

# - Original dictionary
di = {'name': 'Bruce', 'job': 'businessman', 'age': 32}
print('Original dictionary:\t', di)


# - sorted(dictionary) gives you the sorted list of keys
di = {'name': 'Bruce', 'job': 'businessman', 'age': 32}
s_di = sorted(di)
print('Sorted dictionary:\t', s_di )


# - Sort based on a specific criteria

# - Original list
lst = [-9,1,-8,2,-7,-3,-6,4,5]
print('Original list:\t', lst )

# - Sort list
s_lst = sorted(lst)
print('Sorted list:\t', s_lst )

# - Sort list with absolute value as key
s_lst = sorted(lst, key=abs)
print('Sorted list:\t', s_lst )

#########################

####################################
# - List of custom class objects - #
####################################

class Employee():
    def __init__ (self, name, age, salary):
        self.name   = name
        self.age    = age
        self.salary = salary

    def __repr__ (self):
        return '({},{},{})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl',  37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John',  43, 90000)

employees = [e1,e2,e3]
print('Employees:\t', employees )

# Naiveliy try to sort the class 
# s_employees = sorted(employees)
# TypeError: unorderable types: Employee() < Employee()

# - Custom key function to order insatnces of the class
def e_sort(emp):
    return emp.name

# - Sort the list
s_employees = sorted(employees, key=e_sort)
print('Employees:\t', s_employees )

def e_sort(emp):
    return emp.salary

# - Sort the list in reverse
s_employees = sorted(employees, key=e_sort, reverse=True)
print('Employees:\t', s_employees )


# - We can also sort using lambda functions
s_employees = sorted(employees, key=lambda e: e.age)
print('Employees:\t', s_employees )


# Attribute getter
from operator import attrgetter

# - We can also sort using attrgetter
s_employees = sorted(employees, key=attrgetter('salary'))
print('Employees:\t', s_employees )

