# SQLite 3 documentation

## Basic

### Create a database

Database living in a physical file:

~~~~
database_file = 'employee.db'
conn = sqlite3.connect(database_file)
~~~~

Database living in RAM:

~~~~
conn = sqlite3.connect(':memory:')
~~~~

### Passing variables into a SQL command

#### Unsafe(!) way to create SQL queries:

~~~~
c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_2.last, emp_1.pay))
~~~~

#### Safe way to create SQL queries:

~~~~
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_2.last, emp_1.pay) )
~~~~

~~~~
dict = { 'first': emp_1.first, 'last': emp_1.last, 'pay': emp_2.pay }
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", dict)
~~~~


## References

[Datatypes in SQLite Version 3][datatypes]

[datatypes]: https://sqlite.org/datatype3.html
