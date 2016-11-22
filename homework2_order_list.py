# rearrange the inventory to create an order list used in homework2.py

from random import randint


inventory = [("Ford", "Ka", 3),
                ("Ford", "Focus Sedan", 7),
                ("Ford", "Focus Estate", 2),
                ("Honda", "Integra", 1),
                ("Honda", "Civic", 5)]

stock = []
for car in inventory:
    stock.append((car[0], car[1]))

print('stock =', stock)

car_id = [randint(0,4) for i in range(15)]

order_list = []
for index, id in enumerate(car_id):
    order_list.append((stock[id][0], stock[id][1], '2016-09-{0:0=2d}'.format(index + 1)))

print(order_list)