eng2de = {}
eng2de['one'] = 'eins'
eng2de['two'] = 'zwei'

print(eng2de)


inventory = { 
  'apples' : 512,
  'bananas' : 100,
}

print(inventory['apples'])

# fruit = input('Please enter the fruit you want to query: ')

# print(inventory[fruit])


# new_fruit = input('Please add new fruit to add to inventory: ')
# count = int(input('Please enter the number of that fruit in store: '))

# inventory[new_fruit] = count

# print(inventory)

for fruit, count in inventory.items():
  print(f'There are {count} {fruit} in store')

sum_of_fruits = 0
for count in inventory.values():
  sum_of_fruits += count

for fruit in inventory.keys():
  pass

print(f'There are {sum_of_fruits} fruits in store')

meat_inventory = {
  'Steaks' : 13,
  'Salami' : 20
}

overall_inventory = {}
overall_inventory['fruits'] = inventory
overall_inventory['meat'] = meat_inventory



for fruit, count in overall_inventory['fruits'].items():
  print(f'There are {count} {fruit} in store')
