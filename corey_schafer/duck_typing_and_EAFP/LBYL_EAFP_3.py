################################################################
### ---            Look before you leap (LBYL) vs.       --- ###
### --- Easier to ask forgiveness than permission (EAFP) --- ###
################################################################

my_list = [1, 2, 3, 4, 5]

# - LBYL

if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist.')

# - EAFP

try:
    print(my_list[5])
except IndexError:
    print('That index does not exist.')

