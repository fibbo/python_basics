import json

inventory = {
    'apples': 324,
    'bananas': 234,
}

inventory_as_string = json.dumps(inventory)

print(type(inventory))
print(type(inventory_as_string))

print(inventory)
print(inventory_as_string)

file = open('inventory.txt', 'w')
file.write(inventory_as_string)
file.close()