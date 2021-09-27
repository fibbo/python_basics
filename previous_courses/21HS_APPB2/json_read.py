import json

inventory = {}
print(inventory)

with open("inventory.txt", "r") as f:
    for line in f:
        inventory = json.loads(line)


for fruit, count in inventory.items():
    print(f"There are {count} {fruit} in store")
