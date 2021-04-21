import json

inventory = {}

with open('json.data', 'r') as json_file:
    for line in json_file:
        inventory = json.loads(line)


for fruit, amount in inventory.items():
    print(f'There are {amount} {fruit} in store')