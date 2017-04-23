########################
### --- Closures --- ###
########################

# - Definition of a closure (from Wikipedia):
# A closure is a record storing a function[a] together with an environment:[1] a
# mapping associating each free variable of the function (variables that are used
# locally, but defined in an enclosing scope) with the value or reference to which
# the name was bound when the closure was created.[b] A closure—unlike a plain
# function—allows the function to access those captured variables through the
# closure's copies of their values or references, even when the function is
# invoked outside their scope.

def outer_func():
	message = 'First'  # <- This is a free variable,
                       # we have access to this in the
	def inner_func():  # inner_function()
		print(message)

	return inner_func()

outer_func()

print("End of first segment.\n")
#################################

def outer_func():
	message = 'Second' # <- This is a free variable,
                       # we have access to this in the
	def inner_func():  # inner_function()
		print(message)

	return inner_func  # <- return the function w/o executing it

my_func = outer_func() # <- my_func is actually a function now

print(my_func)
print(my_func.__name__)

my_func()
my_func()
my_func()

print("End of second segment.\n")
#################################

def outer_func( msg ):
	message = msg # <- This is a free variable,
                       # we have access to this in the
	def inner_func():  # inner_function()
		print(message)

	return inner_func  # <- return the function w/o executing it

hello_func = outer_func('Hello.')
hi_func = outer_func('Hi.')

print(hello_func)
print(hi_func.__name__)

hello_func()
hi_func()

print("End of third segment.\n")
