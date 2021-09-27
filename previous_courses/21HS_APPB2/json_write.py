import json

inventory = {"apples": 100, "bananas": 320}
print(inventory)
inventory_string = json.dumps(inventory)

with open("inventory.txt", "w") as f:
    f.write(inventory_string)
