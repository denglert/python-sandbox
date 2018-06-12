#!/usr/bin/env python

@profile
def generator_vs_list():
    
    numbers = 100000


    a = [i for i in range(numbers)]

    del a

    b = (i for i in range(numbers))

    del b


generator_vs_list()
