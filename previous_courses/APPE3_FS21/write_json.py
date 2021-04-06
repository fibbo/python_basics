import json


inventory = { 'Apples': 512, 'Bananas': 100 }

print(inventory)

inventory_as_string = json.dumps(inventory)

with open('inventory.txt', 'w') as f:
  f.write(inventory_as_string)