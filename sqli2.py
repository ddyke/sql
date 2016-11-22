"""
Again, start with writing out the steps in plain English.

1. Import the sqlite3 library.
2. Connect to the database.
3. Establish a cursor.

4. Using an infinite loop, continue to ask the user to enter the number of an operation that they’d like to perform.
   If they enter a number associated with a SQL function, then run that function.
   However, if they enter number not associated with a function, ask them to enter another number.
   If they enter the number 5, exit the program.

Clearly, step 4 needs to be broken up into multiple steps. Do that before you start writing any code.

Good luck!
"""

import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as conn:
    c = conn.cursor()

    u_input = None
    while u_input is None:
        u_input = input("Input Operation Number (1-4): ")
        try:
            u_input = int(u_input)
            if not 1 <= u_input <= 5:
                print("Input out of range")
                u_input = None
        except ValueError:
            print("Invalid input")
            u_input = None

    if u_input == 5:
        print("Closing the program")
        exit()


    action_list = ['sum', 'max', 'min', 'avg']
    sql = "SELECT {}(num) FROM integers".format(action_list[u_input - 1])

    c.execute(sql)
    output = c.fetchone()
    print("{}: {}".format(action_list[u_input - 1], output[0]))





