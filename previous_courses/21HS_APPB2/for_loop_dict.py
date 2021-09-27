inventory = {"apples": 100, "bananas": 320, "salads": 7, "carrots": 20}

for fruit, count in inventory.items():
    print(f"There are {count} {fruit} in store")


for fruit in inventory.keys():
    print(fruit)

for count in inventory.values():
    print(count)


store_inventory = {
    "fruits": {"apples": 100, "bananas": 210},
    "vegetables": {"salads": 7, "carrots": 20},
}

for vegetable, count in store_inventory["vegetables"].items():
    print(vegetable, count)
