############################
### --- Named tuples --- ###
############################

from collections import namedtuple

### --- Tuple --- ###

# Advantage:
# - Immutable, can't change the values

color_tuple = (55, 155, 255)

print( color_tuple[0] )

### --- Dictionaries --- ###
# Disadvantage:
# - Requires more typing
# - You need to define new colours also in this format
#
color_dict = {'red': 55, 'green': 155, 'blue': 255}

print( color_dict['red'] )

### --- Named tuple --- ###
# Advantage:
# - Has the nice features of both tuple and dictionary 
# - You define it only once typing in the names, but can access the element with 
#   both [int] and .name 

Color_ntuple = namedtuple('Color', ['red', 'green', 'blue'])

color_ntuple = Color_ntuple(55, 155, 255)          
color_ntuple = Color_ntuple(red=55, green=155, blue=255)

print( "color_ntuple[0]",  color_ntuple[0] )
print( "color_ntuple.red", color_ntuple.red )
