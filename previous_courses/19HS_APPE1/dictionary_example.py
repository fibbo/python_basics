inventory = {
    "apples": 430,
    "bananas": 312,
}
if "apples" in inventory:
    # inventory['apples'] = inventory['apples'] + 100
    inventory["apples"] += 100
else:
    inventory["apples"] = 100


print(inventory["apples"])

for item_name, number_in_stock in inventory.items():
    print("There are {} of {} in stock".format(number_in_stock, item_name))
    # print('There are ' + str(number_in_stock) + ' of ' etc...)
