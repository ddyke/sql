# Create SQLite3 database and table

import sqlite3

# create a new database if it doesn't already exist
conn = sqlite3.connect("cars.db")

# create a cursor object
cursor = conn.cursor()

# create a table
cursor.execute("CREATE TABLE inventory(Make TEXT, Model TEXT, Quantity INT)")

# close the database connection
conn.close()

