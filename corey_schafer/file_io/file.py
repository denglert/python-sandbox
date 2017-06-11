#########################
### --- File I/O  --- ###
#########################

# - Open file for reading
# open(, x), where x could be:
# 'r'  : read
# 'w'  : write
# 'a'  : append
# 'r+' : read and write

f = open('test.txt', 'r')

print('f.name: ', f.name)
print('f.mode: ', f.mode)
print('f.closed: ', f.closed)

f.close()

print('f.closed: ', f.closed)

### --- Contents manager --- ###
# - Considered a better practice

with open('test.txt', 'r') as f:
#    f_contents = f.read()
#    print('f_contents: \n', f_contents)

#    f_contents = f.readlines()
#    print('f_contents: \n', f_contents)

#    f_contents = f.readline()
#    print('f_contents: \n', f_contents, end='')

#    f_contents = f.readline()
#    print('f_contents: \n', f_contents, end='')

#    for line in f:
#        print(line, end='')

    # - Read in a 100 characters
#    f_contents = f.read(100)
#    print(f_contents, end='')

#    f_contents = f.read(100)
#    print(f_contents, end='')


#    size_to_read = 10
#    f_contents = f.read(size_to_read)

#    while len(f_contents) > 0:
#        print(f_contents, end='*')
#        f_contents = f.read(size_to_read)

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='*')

    # - Move to position 0
    f.seek(0)
    print('\nf.tell(): ', f.tell())

    f_contents = f.read(size_to_read)
    print(f_contents, end='*')

    print('\nf.tell(): ', f.tell())

#print('f.closed: ', f.closed)
#print('f.read: ', f.read())

#################################

### --- Writing to files --- ###

#with open('test2.txt', 'w') as f:
#    f.write('Test')
#    f.seek(0)
#    f.write('Test')

### --- Read and write --- ###

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


### --- Copy an image --- ###

# - This doesn't work
#with open('doge.jpg', 'r') as rf:
#    with open('doge_copy.jpg', 'w') as wf:
#        for line in rf:
#            wf.write(line)

# - We have to open file in binary mode 'rb' and 'wb'
with open('doge.jpg', 'rb') as rf:
    with open('doge_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0: 
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
