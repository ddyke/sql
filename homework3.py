"""
Using the COUNT() function, calculate the total number of orders for each make and model.
Output the car’s make and model on one line, the quantity on another line,
and then the order count on the next line.
The latter is a bit difficult, but please try it first before looking at my answer.
"""

import sqlite3

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    sql_count = "SELECT make, model, count(model) FROM orders GROUP BY model"
    c.execute(sql_count)
    orders = c.fetchall()
    for order in orders:
        print("Make: {}, Model: {}".format(order[0], order[1]))
        print("Number of orders: {}".format(order[2]))
