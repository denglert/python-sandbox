#!/usr/bin/env python

#import memory_profiler

@profile
def function_to_be_tested(nlength=1000):

    a = [i for i in range(nlength)]

    b = [i for i in range(nlength*10)]

    c = [i for i in range(nlength*100)]


function_to_be_tested()


