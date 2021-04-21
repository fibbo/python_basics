import json

inventory = { 'apples' : 512, 'bananas' : 100}

inventory_as_string = json.dumps(inventory)

with open('inventory.txt', 'w') as f:
  f.write(inventory_as_string)