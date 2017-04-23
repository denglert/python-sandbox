################################
### --- str() and repr() --- ###
################################

# - Functions introduced:
# * repr()
# * str()

# - Summary:
# - The goal of repr is to be unambiguous.
# - The goal of str is to be readable.

a = [1,2,3,4]
b = 'sample string'

print('str(a): ', str(a) )
print('repr(a): ', repr(a)) 

print('str(b): ', str(b) )
print('repr(b): ', repr(b)) 

#########################################
print()

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

# - See the difference between the two.
# - The output of repr() is more suited to be run as a python command.
# - repr() is really meant for developers, e.g. while debugging, whereas
# - str() is more user friendly.

print('str(a)', str(a) )
print('str(b)', str(b) )

print('repr(a)', repr(a) )
print('repr(b)', repr(b) )
