################################################################
### ---            Look before you leap (LBYL) vs.       --- ### 
### --- Easier to ask forgiveness than permission (EAFP) --- ###
################################################################

# - Python docs:
# - https://docs.python.org/2/glossary.html#term-eafp

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


# - Duck typed, look before you leap (LBYL), non-pyhonic.
# - Asking for permissions all the time
def quack_and_fly_duck_typing_lbyl(thing):

	if hasattr(thing, 'quack'):
	    if callable(thing.quack):
	        thing.quack()
	
	if hasattr(thing, 'fly'):
	    if callable(thing.fly):
	        thing.fly()

	print()


# - Easier to ask forgiveness than permission (EAFP), pythonic.
def quack_and_fly_duck_typing_eafp(thing):

	try:
	    thing.quack()
	    thing.fly()
	    thing.bark()
	except AttributeError as e:
	    print(e)

d = Duck()
p = Person()

print('# - Look before you leap (LBYL), non-pythonic.\n')

quack_and_fly_duck_typing_lbyl(d)

print('# - Easier to ask forgiveness than permission, pythonic.\n')

quack_and_fly_duck_typing_eafp(p)
