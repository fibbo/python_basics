inventory = {
    'apples': 312,
    'bananas': 420
}

for fruit, amount in inventory.items():
    print('There are {} {} in store'.format(amount, fruit))


for fruit in inventory.keys():
    print('There are {}'.format(fruit))


count = 0
for amount in inventory.values():
    count += amount

print('In total I have {} fruits'.format(count))