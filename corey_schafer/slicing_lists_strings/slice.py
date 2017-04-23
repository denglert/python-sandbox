# Based on: https://www.youtube.com/watch?v=ajrtAuDg3yw

# - This is a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 

# Syntax: list[start:end:step]

# - Print the whole list
print("\nlist:\n{0}".format(my_list) )

# - Print index 0 element
index=0
print("\nlist[{0}]:\n{1}".format(index, my_list[index]) )

# - Print index 5 element
index=5
print("\nlist[{0}]:\n{1}".format(index, my_list[index]) )

# - Print the last element
index=-1
print("\nlist[{0}]:\n{1}".format(index, my_list[index]) )

# - Print the element before the last
index=-2
print("\nlist[{0}]:\n{1}".format(index, my_list[index]) )

# - Print the elements from index 0 to 5
start=0  # 
end=5    # Non-exclusive end! Doesn't include 5
print("\nlist[{0}:{1}]:\n{2}".format(start, end, my_list[start:end]) )

# - Print the elements from index 3 to 8
start=3  # 
end=8    # Non-exclusive end! Doesn't include 5
print("\nlist[{0}:{1}]:\n{2}".format(start, end, my_list[start:end]) )

# - Print the elements from index -7 to 8
start=-7   
end=8     # Non-exclusive end! Doesn't include 5
print("\nlist[{0}:{1}]:\n{2}".format(start, end, my_list[start:end]) )

# - Print all of the elements 
start=None
end=None
print("\nlist[{0}:{1}]:\n{2}".format( start, end, my_list[start:end]) )

# - Print with steps
start=1
end=-3
step=2
print("\nlist[{0}:{1}:{2}]:\n{3}".format( start, end, step, my_list[start:end:step]) )

# - Print with steps
start=1
end=-3
step=-2
print("\nlist[{0}:{1}:{2}]:\n{3}".format( start, end, step, my_list[start:end:step]) )

# - Print with steps
start=-3
end=1
step=-2
print("\nlist[{0}:{1}:{2}]:\n{3}".format( start, end, step, my_list[start:end:step]) )

# - Print with steps
start=None
end=None
step=-1
print("\nlist[{0}:{1}:{2}]:\n{3}".format( start, end, step, my_list[start:end:step]) )

###############################
### --- Slicing strings --- ###
###############################

string = 'http://coreyms.com'

# - Print string
print( "\nstring:\n{0}".format( string ) )

# - Print string starting at index -4
start=-4
print( "\nstring[{0}]:\n{1}".format( start, string[start:] ) )

# - Print string starting at index 7
start=7
print( "\nstring[{0}]:\n{1}".format( start, string[start:] ) )

# - Print string starting at index 7
start=7
end=-4
print( "\nstring[{0}:{1}]:\n{2}".format( start, end, string[start:end] ) )
