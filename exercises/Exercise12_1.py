import json

address_book_dict = {}
while True:
    name = input('Enter name or type exit to quit: ')
    if name == 'exit':
        break
    phone = input('Phone: ')
    address_book_dict[name] = phone

with open('address_book.txt', 'w') as address_book_file :
    address_book_json = json.dumps(address_book_dict)
    address_book_file.write(address_book_json)
