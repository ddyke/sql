import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA  ', 800000)")

conn.commit()

conn.close()

"""
FOR concise script

with sqlite3.connect("new.db") as conn:
    conn.cursor = conn.cursor()
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA  ', 800000)")
"""