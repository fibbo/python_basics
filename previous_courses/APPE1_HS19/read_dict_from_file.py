import json


file = open('inventory.txt', 'r')

inventory = {}

for line in file:
    inventory = json.loads(line.strip())

print(inventory['apples'])