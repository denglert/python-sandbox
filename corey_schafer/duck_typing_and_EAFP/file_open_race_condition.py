import os

my_file = 'test.txt'

# - LBYL (non-pythonic), which has race condition

if os.access(my_file, os.R_OK):
	with open(my_file) as f:
		print(f.read())
else:
	print('File can not be accessed.')

# - EAFP (pythonic), no race condition

try:
	f = open(my_file)
except IOError as e:
	print('File can not be accessed.')
else:
	with f:
		print(f.read())
