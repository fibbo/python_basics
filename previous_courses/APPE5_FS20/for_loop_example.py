numbers = list(range(20))

for number in numbers:
    print(2 * number)


names = ['Tom', 'Jerry', 'Anna']

for x in names:
    print(x)

# This is actually intended to work:
# https://eli.thegreenplace.net/2015/the-scope-of-index-variables-in-pythons-for-loops/
x += 'test'

print(x)