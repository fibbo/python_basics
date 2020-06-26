import json

address_book = {}

with open('address_book.txt', 'r') as f:
    for line in f:
        line = line.strip()
        address_book = json.loads(line)

while True:
    name = input('Please enter the name or type exit to quit: ')
    if name == 'exit':
        break

    address_book[name] = input('Enter the phone number: ')

address_book_string = json.dumps(address_book)

with open('address_book.txt', 'w') as f:
    f.write(address_book_string)