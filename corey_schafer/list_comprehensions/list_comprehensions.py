#####################
### --- List  --- ###
#####################

nums = [1,2,3,4,5,6,7,8,9]

# - I want 'n' for each 'n' in nums
# - With for loop
my_list = []

for n in nums:
    my_list.append(n)

print("\nmy_list:\n{0}".format( my_list ) )

# - I want 'n' for each 'n' in nums
# - With list comprehension
# - [] = list

my_list = [n for n in nums] 
print("\nmy_list:\n{0}".format( my_list ) )

# - I want 'n*n' for each 'n' in nums
# - With for loop
my_list = []

for n in nums:
    my_list.append(n*n)

print("\nmy_list:\n{0}".format( my_list ) )

# - I want 'n*n' for each 'n' in nums
# - With for loop

my_list = [n*n for n in nums] 
print("\nmy_list:\n{0}".format( my_list ) )

# - With maps and lambdas
# - map: run everything in a list through a certain function
# - lambda: anonymous function

my_list = list( map(lambda n: n*n, nums ) )
print("\nmy_list:\n{0}".format( my_list ) )

# - With for loop
# - I want 'n' for each 'n' in nums if 'n' is even

my_list = []

for n in nums:
    if n % 2 == 0:
        my_list.append(n)

print("\nmy_list:\n{0}".format( my_list ) )

# - I want 'n' for each 'n' in nums if 'n' is even
# - With list comprehension
# - [] = list

my_list = [n for n in nums if n%2 == 0] 
print("\nmy_list:\n{0}".format( my_list ) )

# - I want 'n' for each 'n' in nums if 'n' is even
# - Using map and filter functions

my_list = list( filter(lambda n: n%2 == 0, nums ) )
print("\nmy_list:\n{0}".format( my_list ) )


###########################################


# - I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# - With for loops
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append( (letter,num) )

print("\nmy_list:\n{0}".format( my_list ) )

# - I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# - With list comprehensions

my_list = [ (letter,num) for letter in 'abcd' for number in range (4) ]
print("\nmy_list:\n{0}".format( my_list ) )

#########################
# --- Dictionairies --- #
#########################

names  = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

zipped_tuple = list( zip (names, heroes ) )
print("\nzipped_tupel:\n{0}".format(zipped_tuple))

# - Dictionary with loops
my_dict = {}

for name, hero in zip (names, heroes):
    my_dict[name] = hero

print("\nmy_dict:\n{0}".format(my_dict))

# - Dictionary comprehension 
my_dict = { name: hero for name, hero in zip(names, heroes) }
print("\nmy_dict:\n{0}".format(my_dict))

# - Dictionary comprehension with conditional
my_dict = { name: hero for name, hero in zip(names, heroes)  if name != 'Peter'}
print("\nmy_dict:\n{0}".format(my_dict))

################
# --- Sets --- #
################

nums = [1,1,2,1,3,4,3,4,5,5,6,7,9,9]  # This is a list


# -  With a for loop
my_set = set () # set definition
for n in nums:
    my_set.add(n)
print("\nmy_set:\n{0}".format(my_set))

# - With set comprehension
my_set = {n for n in nums}
print("\nmy_set:\n{0}".format(my_set))


#################
# - Generator - #
#################


nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)

