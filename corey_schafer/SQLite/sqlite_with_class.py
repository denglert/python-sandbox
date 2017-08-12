#!/usr/bin/env python

from sql_util import database
from employee import  Employee

emp_1 = Employee('John', 'Wick', 100000)
emp_2 = Employee('Jane', 'Doe', 90000)


db = database()

db.insert_emp(emp_1)
db.insert_emp(emp_2)

emp_query = db.get_emps_by_name('Doe')

print(emp_query)
