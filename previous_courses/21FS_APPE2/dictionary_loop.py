inventory = {"apples": 12, "bananas": 100}

some_dictionary = {"value1": [12, 45, 67]}

# for book, cost in inventory.items():
#   print('There are {} {} in stock'.format(cost, book))


# for number in some_dictionary['value1']:
# print(number)

for fruit, number in inventory.items():
    print("There are {} in storage".format(fruit))
