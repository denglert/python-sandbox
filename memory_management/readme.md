# Memory management in python

Author: Nina Zakharenko
Title: Memory Management in Python - The Basics
Venue: PyCon 2016

Video: https://www.youtube.com/watch?v=F6u5rhUQ6dU

Ways to decrease the reference count:
- remove the reference with`del`
- change reference
- going out of scope

Note: `del` removes the name as a reference to that object, therefore decreases the reference count.


Internally every python objects holds three things:
- its type
- its value
- reference count
