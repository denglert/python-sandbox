my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
else: # else here = no break
    print('Hit the for/else statement')

#######################################
print('\n##########################\n')

for i in my_list:
    print(i)
    if i == 3:
        break
else: # else here = no break
    print('Hit the for/else statement')

#######################################
print('\n##########################\n')

for i in my_list:
    print(i)
    if i == 6:
        break
else: # else here = no break
    print('Hit the for/else statement')

#######################################
print('\n##########################\n')

# - This also works for while loop

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print('Hit the for/else statement')


#######################################
print('\n##########################\n')

# - This also works for while loop

i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print('Hit the for/else statement')
