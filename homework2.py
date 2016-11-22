"""
Continues from homework.py
Add another table to accompany your “inventory” table called “orders”.
This table should have the following fields: “make”, “model”, and “order_date”.
Make sure to only include makes and models for the cars found in the inventory table.
Add 15 records (3 for each car), each with a separate order date (YYYY-MM-DD).
Finally output the car’s make and model on one line, the quantity on another line,
and then the order_dates on subsequent lines below that.”

Model Make Quantity
('Ford', 'Ka', 3)
('Ford', 'Focus Sedan', 7)
('Ford', 'Focus Estate', 4)
('Honda', 'Integra', 0)
('Honda', 'Civic', 5)
"""
import sqlite3


with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    #c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    # ordered cars list doesn't conform to the requirement (3 for each car) but it's ok.

    stock = [('Ford', 'Ka'),
             ('Ford', 'Focus Sedan'),
             ('Ford', 'Focus Estate'),
             ('Honda', 'Integra'),
             ('Honda', 'Civic')]

    ordered_cars = [('Honda', 'Integra', '2016-09-01'),
                    ('Honda', 'Integra', '2016-09-02'),
                    ('Honda', 'Civic', '2016-09-03'),
                    ('Honda', 'Integra', '2016-09-04'),
                    ('Honda', 'Integra', '2016-09-05'),
                    ('Honda', 'Integra', '2016-09-06'),
                    ('Honda', 'Civic', '2016-09-07'),
                    ('Ford', 'Ka', '2016-09-08'),
                    ('Ford', 'Focus Estate', '2016-09-09'),
                    ('Honda', 'Civic', '2016-09-10'),
                    ('Ford', 'Focus Estate', '2016-09-11'),
                    ('Honda', 'Civic', '2016-09-12'),
                    ('Ford', 'Focus Sedan', '2016-09-13'),
                    ('Ford', 'Ka', '2016-09-14'),
                    ('Honda', 'Integra', '2016-09-15')]

    #c.executemany("INSERT INTO orders VALUES(?,?,?)", ordered_cars)

    # join data from 2 tables for each model
    for car in stock:
        model = car[1]
        c.execute("""SELECT orders.make, orders.model, inventory.Quantity, orders.order_date from inventory,
        orders WHERE orders.model=inventory.Model AND orders.model='{}'""".format(model))
        rows = c.fetchall()
        print("Make: {}, Model: {}".format(rows[0][0], rows[0][1]))
        print("Stock: {}".format(rows[0][2]))
        print("Order Dates:")
        for row in rows:
            print(row[3])




