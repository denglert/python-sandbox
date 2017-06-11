###########################
###  --- Generators --- ###
###########################

# - Generators advantages:
# Generators don't hold the entire result in memory.
# It yields one result at a time.
# It has better performance compared to lists.


# - square_numbers function
# takes in a list of numbers
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])  # [1, 4, 9, 16, 25]

print(my_nums)

### - Converting this to a generator --- ###

def square_numbers(nums):
    for i in nums:
        yield (i*i)       # this yield keyword makes it a generator

# This is more readable compared to the previous function

my_nums = square_numbers([1,2,3,4,5])  # [1, 4, 9, 16, 25]

print(my_nums)   # generator object

# See the following:
#print( next(my_nums) )  # asking for the next result
#print( next(my_nums) )  # asking for the next result
#print( next(my_nums) )  # asking for the next result
#print( next(my_nums) )  # asking for the next result
#print( next(my_nums) )  # asking for the next result
#print( next(my_nums) )  # asking for the next result, exception StopIteration

for num in my_nums:
    print(num)       # for loop knows when to stops

### --- With list comprehension --- ###

print("\nList comprehension.")

my_nums = [ x*x for x in [1,2,3,4,5] ]

print(my_nums)

for num in my_nums:
    print(num)

### --- With generator comprehension --- ###

print("\nGenerator comprehension.")

my_nums = ( x*x for x in [1,2,3,4,5] )

print(my_nums)    # generator object

#for num in my_nums:
#    print(num)

# - Converting a generator into a list
print( list(my_nums) )  # you loose performance here.
