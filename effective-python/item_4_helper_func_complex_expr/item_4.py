#!/usr/bin/env python

from urllib.parse import parse_qs


# - Decode the query string from an url

query_string = 'red=5&blue=0&green='
my_values = parse_qs(query_string,
                     keep_blank_values=True)

print( repr(my_values) )

# - You can use `dict.get(key)` to extract the value for a key in a dictionary
# - This returns a list
print("Red:     ", my_values.get('red') )
print("Green:   ", my_values.get('green') )
print("Opacity: ", my_values.get('opacity') )

red     = my_values.get('red',     [""])[0] or 0
green   = my_values.get('green',   [""])[0] or 0
opacity = my_values.get('opacity', [""])[0] or 0

print('red:     %r' % red)
print('green:   %r' % green)
print('opacity: %r' % opacity)
