###############################
### --- Try and except  --- ###
###############################

# - Default format

try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass

# - Usually you only use the 'try' and 'except' part

try:
    pass
except Exception:
    pass

# - Example
# You need to put the more specific exception errors (e.g. FileNotFound) first
# and the more general ones (Exception) last

try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError:                    
    print('Sorry. This file does not exists')
except Exception:
    print('Sorry. Something went wrong.')


###############################
print("\nSecond method with 'as e'.")

try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)


###############################
print("\nNow we also try to use 'else'.")

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:                # else clause is executed if the try didn't give any errors
    print(f.read())
    f.close()

###############################
print("\nAnd finally 'finally'.")

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:                # else clause is executed if the try didn't give any errors
    print(f.read())
    f.close()
finally:             # finally clause is executed no matter what
    print("Executing finally...")

###############################
print("\nWe can also raise our own exceptions.")

try:
    f = open('corrupt_file.txt')
    if f.name == "corrupt_file.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Corrupt file!")
else:                # else clause is executed if the try didn't give any errors
    print(f.read())
    f.close()
finally:             # finally clause is executed no matter what
    print("Executing finally...")

# Q: How can we define custom exception?
