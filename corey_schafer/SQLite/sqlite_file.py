import sqlite3
from employee import  Employee


database_file = 'employee.db'
# - Create a database living in physical file.
conn = sqlite3.connect(database_file)


# - Create a database living only in memory
conn = sqlite3.connect(database_file)

c = conn.cursor()

# - Create an employee table
#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")


emp_1 = Employee('John', 'Wick', 100000)
emp_2 = Employee('Jane', 'Doe', 90000)

print(emp_1)

# - Bad practice: String formatting
# - DO NOT DO THIS!
# - THIS IS VULNERABLE TO SQL INJECTION ATTACKS
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_2.last, emp_1.pay))

# - Secure method #1:
# - DB API placeholders: ?
# - Pass the variables as an argument of .execute() in form of a tuple.
#c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_2.last, emp_1.pay) )


# - Secure method #2:
# - DB API placeholders: :
# - Pass variables as an argument of .execute() in form of a dictionary.
#dict = { 'first': emp_1.first, 'last': emp_1.last, 'pay': emp_2.pay }
#c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", dict)

# c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
# c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

#c.execute("SELECT * FROM employees WHERE last='Schafer'")
#c.execute("SELECT * FROM employees")
c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

print(c.fetchall())

# c.fetchone()
# c.fetchmany(5)
# c.fetchall()

########################################

# - This commits the current transaction
conn.commit()

# - Close the connection to the database
conn.close()
