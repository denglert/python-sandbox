#####################################
### --- First-class functions --- ###
#####################################

# First-class functions:
# "A programming language is said to have first-class function if it treats
# functions as first-class citizens."

# First class citizens:
# "A first-class citizen (sometimes called first-class objects) in a programming
# language is an entity which supports all the operations generally available to
# other entities. These operations typically inclued being passed as an
# argument, returned from a function, and assigned to a variable."

############################################
# Assigning the return variable 'x*x' to the variable 'f'

def square(x):
    return x*x

def cube(x):
    return x*x*x

f = square(5)

print('square: ', square)
print('f: ', f)

print('End of first segment.\n')
############################################
# Assigning the function itself 'square' to the 'f' variable

f = square

print('square: ', square)
print('f: ', f)
print('f(5): ', f(5))
print('End of second segment.\n')

######################################################
# -  So far we assigned a function to a variable, but we can also pass
# functions as arguments and return functions as the result of other functions.
# Let's take a look at both of these examples.

# Higher-order function: a function which accepts other functions as arguments,
# or returns functions as their result

# - Example 1: map(function, array) function
# Passing a function as an argument to another function

def my_map (func, arg_list):
    result = []
    for i in arg_list:
        result.append( func(i) )
    return result

squares = my_map( square, [1,2,3,4,5])
cubes   = my_map( cube, [1,2,3,4,5])

print('squares: ', squares)
print('cubes: ', cubes)

print('End of third segment.\n')
# - Example 2: logger function
# Return a function from another function


def logger( msg ):

    def log_message():
        print('Log:', msg)

    return log_message

log_hi = logger('Hi!')
log_hi()

print('End of third segment.\n')


######################################################
# - Example 3: html tag
# Return a function from another function

def html_tag( tag ):
	 
	 def wrap_text( msg ):
		  print( '<{0}>{1}</{0}>'.format(tag, msg) )

	 return wrap_text

print_h1 = html_tag('h1')

print_h1('Test headline!')
print_h1('Another headline!')

print_p = html_tag('p')
print_p( 'Test paragraph!' )
