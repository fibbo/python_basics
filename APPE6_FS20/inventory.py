def add_to_inventory(inventory, product, number):
    if product in inventory:
        inventory[product] += number
    else:
        inventory[product] = number


inventory = {
'apples': 200,
'bananas': 120,
}

if 'apples' in inventory:
    inventory['apples'] += 100
else:
    inventory['apples'] = 100

add_to_inventory(inventory, 'cherries', 1200)

for fruit, stored_amount in inventory.items():
    print('{}: {} in store'.format(fruit, stored_amount))
