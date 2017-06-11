###########################
### --- Duck Typing --- ###
###########################

# - Wikipedia:

# - In computer programming, duck typing is an application of the duck test in type
# - safety. It requires that type checking be deferred to runtime, and is
# - implemented by means of dynamic typing or reflection.

# - If an object walks like a duck and quacks like a duck then it's a duck!

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


# - Not duck typed (non-pythonic).
def quack_and_fly_duck_typing_non_pythonic(thing):

	if isinstance(thing, Duck):
	    thing.quack()
	    thing.fly()
	else:
	    print('This is not a duck!')

	print()


# - Duck typed (pythonic).
def quack_and_fly_duck_typing_pythonic(thing):

	thing.quack()
	thing.fly()

	print()

d = Duck()
p = Person()

print('# - Non duck typed, non-pythonic.\n')

quack_and_fly_duck_typing_non_pythonic(d)
quack_and_fly_duck_typing_non_pythonic(p)

print('# - Duck typed, pythonic.\n')

quack_and_fly_duck_typing_pythonic(d)
quack_and_fly_duck_typing_pythonic(p)
