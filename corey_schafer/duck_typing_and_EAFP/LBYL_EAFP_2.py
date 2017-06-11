################################################################
### ---            Look before you leap (LBYL) vs.       --- ### 
### --- Easier to ask forgiveness than permission (EAFP) --- ###
################################################################


person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
#person = {'name': 'Jess', 'age': 23}

print('LBYL:\n')

# - LBYL (non-pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm name {name}. I'm {age} years old and I am a {job}.".format(**person))
else:
    print('Missing some keys.')

print('\nEAFP:\n')

# - EAFP (pythonic)
try:
    print("I'm name {name}. I'm {age} years old and I am a {job}.".format(**person))
except KeyError as e:
    print('Missing {} key.'.format(e))

################
print('\nInducing exception:\n')

person = {'name': 'Jess', 'age': 23}

# - EAFP (pythonic)
try:
    print("I'm name {name}. I'm {age} years old and I am a {job}.".format(**person))
except KeyError as e:
    print('Missing {} key.'.format(e))

print('\nEven if there is an exception the program continues.')
print('\nWhereas if you directly call the print on the dictionary missing keys you get this:')
print("I'm name {name}. I'm {age} years old and I am a {job}.".format(**person))
