import os

os.chdir('files-to-be-renamed')

for f in os.listdir():
    f_basename, f_ext = os.path.splitext(f)
    print( "\nBasename and extension split." )
    print( f_basename )
    print( f_ext )

    print( "\nSplitting at -" )
    f_title, f_course, f_num = f_basename.split('-')
    print( f_title )
    print( f_course )
    print( f_num )

    print( "\nStripping of spaces." )
    print( "Filling with zeros." )
    f_title   = f_title.strip()
    f_course  = f_course.strip()
    f_num     = f_num.strip()[1:].zfill(2)

    new_f_name = '{}-{}{}'.format( f_num, f_title, f_ext )
    print( new_f_name )

#    os.rename(f, new_f_name)
