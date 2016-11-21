import sqlite3

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()
    cities = [('Boston', 'MA', 600000),
              ('Chicago', 'IL', 2700000),
              ('Houston', 'TX', 2100000),
              ('Phoenix', 'AL', 1500000)]
    cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
