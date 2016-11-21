# Try/Except handling

import sqlite3

conn = sqlite3.connect("new.db")
c = conn.cursor()

try:
    c.execute('iNSERT INTO populations VALUES("New York City", "NY", 8200000)')
    c.execute('INSERT INTO populations VALUES("San Francisco", "CA", 800000)')

    c.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

c.close()
