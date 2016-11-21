# add csv data to database

import sqlite3, csv

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    employees = csv.reader(open("employees.csv", "rU"))

    #c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    #c.executemany("INSERT INTO employees(firstname, lastname) values(?, ?)", employees)
