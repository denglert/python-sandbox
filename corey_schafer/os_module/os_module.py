import os
from datetime import datetime

# - Lists the names in the current scope
#print( "dir():\n\t", dir() )

# - This returns the module's attributes
#print( "dir(os):\n\t", dir(os) )

# - Print current working directory
print( "os.getcwd():\t", os.getcwd() )

# - Get the value of HOME environment variable
homepath = os.getenv("HOME")
print( "os.getenv('HOME'):\t", homepath )

# - Change directory to homepath
os.chdir(homepath)

# - Print current working directory
print( "os.getcwd():\t", os.getcwd() )

# - List the content of the current working directory
print( "os.listdir():\t", os.listdir() )

# - Join paths
fullpath = os.path.join(homepath,'lib/study/prog/python/sandbox/python-lessons/os_module/')
print( "fullpath:\t", fullpath )

# - Make a directory
# - os.makedir()  doesn't create intermediate folder(s)
# - os.makedirs() also creates intermediate folder(s)
newdirpath = os.path.join(fullpath, 'newdir')
os.makedirs( newdirpath, exist_ok=True )

# - Remove directory
#os.rmdir(newdirpath)

# - Change to fullpath
os.chdir( fullpath )

# - List the content of the current working directory
print( "os.listdir():\t", os.listdir() )

# - Rename files
os.rename('dummyfile', 'dummierfile')

# - Get attributes of a file
attr = os.stat('dummierfile')

# - Print attributes list
print('attributes: ', attr)

# - Get modification time
mod_time = attr.st_mtime

# - Print the modification time in a human readable format (HRF)
print('mod_time: ', datetime.fromtimestamp(mod_time) )

#########

# - Directory tree generator
for dirpath, dirnames, filenames in os.walk( fullpath ):
    print('Currenth path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# - Get environment variable HOME
homepath = os.environ.get('HOME')
print("os.environ.get('HOME'): ", homepath)

# - Get basename of a path
base_name = os.path.basename('/tmp/test.txt')
print("os.path.basename('/tmp/text.txt'): ", base_name)

# - Get directory part of a path
dir_name = os.path.dirname('/tmp/test.txt')
print("os.path.dirname('/tmp/text.txt'): ", dir_name)

# - Get both the basename and directory part of a path
dir_name, base_name = os.path.split('/tmp/test.txt')
print("os.path.split('/tmp/text.txt'): ", os.path.split('/tmp/test.txt'))
print("dir_name: ", dir_name)
print("base_name: ", base_name)

# - Check the existence of a path
isExisting = os.path.exists('/tmp/dfsadf')
print('isExisting: ', isExisting)
isExisting = os.path.exists( os.path.join(homepath,'lib') )
print('isExisting: ', isExisting)

# - Check if a path is directory or a file
isFile = os.path.isfile( os.path.join(homepath,'lib') )
print('isFile: ', isFile)

isDir = os.path.isdir( os.path.join(homepath,'lib') )
print('isDir: ', isDir)

# - Split the path into a 'root' part (dirpath + basename) and an extension part
print("os.path.splitext('/tmp/alphadir/omg.txt'): ", os.path.splitext('/tmp/alphadir/omg.txt'))
