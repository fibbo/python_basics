inventory = { 'apples': 203, 'bananas': 340 }

for fruit, amount in inventory.items():
    print(f'There are {amount} {fruit} in store')


for fruit in inventory.keys():
    print(fruit)


for amount in inventory.values():
    print(amount)



    