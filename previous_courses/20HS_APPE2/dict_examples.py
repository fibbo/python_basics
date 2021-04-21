inventory = {}


inventory['apples'] = 3923
inventory['bananas'] = 123


# article = input('Please enter the article you want to know the storage of: ')

# if article in inventory:
#     print("There are {} {} in storage".format(inventory[article], article))
# else:
#     print("There are no {} in stock.".format(article))


new_article = input('Please enter the name of the new article: ')
number = int(input('Please enter the amount available: '))

if new_article in inventory:
    print("Article already exists - adding to the current value")
    inventory[new_article] += number
else:
    inventory[new_article] = number

print(inventory)