"""
Use three different scripts for these homework assignments:

Using the “inventory” table from the previous homework assignment, add (INSERT) 5 records
(rows of data) to the table. Make sure 3 of the vehicles are Fords while the other 2 are Hondas.
Use any model and quantity for each.
Update the quantity on two of the records, and then output all of the records from the table.
Finally output only records that are for Ford vehicles.
"""

import sqlite3

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    new_cars = [("Ford", "Ka", 3),
                ("Ford", "Focus Sedan", 7),
                ("Ford", "Focus Estate", 2),
                ("Honda", "Integra", 1),
                ("Honda", "Civic", 5)]

    #c.executemany("INSERT INTO inventory VALUES (?, ?, ?)", new_cars)


    c.execute("UPDATE inventory SET Quantity=4 WHERE Model='Focus Estate'")
    c.execute("UPDATE inventory SET Quantity=0 WHERE Model='Integra'")
    c.execute("SELECT * from inventory")

    print("updated: ")
    for r in c.fetchall():
        print(r[0], r[1], r[2])

    c.execute("SELECT * from inventory WHERE Make='Ford'")

    print("Ford cars")
    for r in c.fetchall():
        print(r[0], r[1], r[2])