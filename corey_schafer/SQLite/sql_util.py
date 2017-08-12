#!/usr/bin/env python
import sqlite3
from employee import  Employee


class database:
    """A simple class for managing a sqlite3 database living in memory."""

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c    = self.conn.cursor()


        # - Create table
        self.c.execute("""CREATE TABLE employees (
                           first text,
                           last text,
                           pay integer
                           )""")

    
    def insert_emp(self, emp):
        
        # - `with` context manager
        with self.conn:
            self.c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", { 'first': emp.first, 'last': emp.last, 'pay': emp.pay })
    
    def get_emps_by_name(self, lastname):
        self.c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
        return self.c.fetchall()

    def udpate_pay(self, emp, pay):
        with self.conn:
            self.c.execute("""UPDATE employees SET pay = :pay
                              WHERE first = :first AND last =:last""",
                              { 'first': emp.first, 'last': emp.last, 'pay': pay })
    
    def remove_emp(self, emp):
        with self.conn:
            self.c.execute("DELETE from employees WHERE first = :first AND last = :last",
                            {'first': emp.first, 'last': emp.last})

