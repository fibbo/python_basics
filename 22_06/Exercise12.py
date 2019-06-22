import json

phone_book = {}

address_book_file = open('address_book.txt')
phone_book = json.load(address_book_file)

while True:
    name = input('Please enter the name or type exit to quit: ')
    if name == 'exit':
        break
    phone_number = input('Please enter the phone number: ')
    phone_book[name] = phone_number

address_book_file = open('address_book.txt', 'w')
address_book_string = json.dumps(phone_book)
address_book_file.write(address_book_string)
address_book_file.close()
