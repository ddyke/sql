"""
1. Add 100 random integers, ranging from 0 to 100, to a new database called newnum.db.
2. Prompt the user whether he or she would like to perform an aggregation (AVG, MAX, MIN, or SUM)
   or exit the program altogether.
"""

import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()

    c.execute("DROP TABLE if exists integers")
    c.execute("CREATE TABLE integers(num INT)")
    for i in range(100):
        c.execute("INSERT INTO integers VALUES({})".format(randint(0, 100)))

