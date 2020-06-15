import json

address_book = {}

with open('address_book.txt', 'r') as adress_book_file:
    for line in adress_book_file:
        address_book = json.loads(line.strip())



while True:
    name = input('Please enter the name or type exit to quit: ')
    if name.lower() == 'exit':
        break
    phone_number = input('Please enter the phone number: ')
    address_book[name] = phone_number

address_book_string = json.dumps(address_book)

with open('address_book.txt', 'w') as phone_book_file:
    phone_book_file.write(address_book_string)