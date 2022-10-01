eng2de = {}
eng2de["one"] = "eins"
eng2de["two"] = "zwei"

#     key     sep  value
inventory = {"apples": 430, "bananas": 312, "chocolate": 1000}

# key = input('Please enter key: ')
# value = int(input('Please enter stock number: '))
# print(inventory[key])
# inventory[key] = value

# print(inventory[key])

for (product, number) in inventory.items():
    print("There are {} of {} in stock.".format(number, product))

for number in inventory.values():
    print(number)

for product in inventory.keys():
    print(product)

# print(inventory['bananas'])
# print(inventory['chocolate'])
