# retrieve data, update data, delete data

import sqlite3

with sqlite3.connect("new.db") as conn:

    c = conn.cursor()

    c.execute("SELECT firstname, lastname from employees")


    for r in c.fetchall():      # retrieve all values as a list of tuples
        print(r[0], r[1])

    # updata population table

    c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")

    # delete data

    c.execute("DELETE FROM population WHERE city='Boston'")
    print("\nNEW DATA: \n")

    c.execute("SELECT * FROM population")

    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])