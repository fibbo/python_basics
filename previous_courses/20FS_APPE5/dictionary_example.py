inventory = {}

item = "bananas"


inventory[item] = 200
inventory["apples"] = 340

for product, number in inventory.items():
    print("There are {} {} in stock".format(number, product))

for product in inventory.keys():
    print(product)

for number in inventory.values():
    print(number)
