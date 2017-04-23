import mem_profile
import random
import time

names  = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business', 'Thomas']

print("Memory (before): {}Mb".format( mem_profile.memory_usage_resource() ) )

def people_list( num_people ):
	result = []
	for i in range( num_people ):
		person = {
					 'id': i,
					 'name': random.choice(names),
					 'major': random.choice(majors)
				 }
		result.append(person)
	return result

def people_generator( num_people ):
	for i in range( num_people ):
		person = {
					 'id': i,
					 'name': random.choice(names),
					 'major': random.choice(majors)
				 }
		yield person

t1 = time.clock()
people = people_list(100000)
t2 = time.clock()
print("Took {} seconds for the function using a list".format( t2-t1 ) )

#t3 = time.clock()
#people = people_generator(100000)
#t4 = time.clock()
#print("Took {} seconds for the function using a generator".format( t4-t3 ) )

print("Memory (after): {}Mb".format( mem_profile.memory_usage_resource() ) )

### --- Statistics --- ###

# For 100,000 people

# - List - #
# Memory used: ~ 33 MB
# Time:        ~ 0.68 s

# - Generator - #
# Memory used: ~ 0MB
# Time:        ~ 3e-6 s
