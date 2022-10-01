import json

inventory = {"apples": 100, "bananas": 2340}

inventory_string = json.dumps(inventory)

with open("json.data", "w") as json_file:
    json_file.write(inventory_string)

print(inventory)
