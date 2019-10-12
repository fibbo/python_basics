import json

address_book = {}

try:
    file = open('address_book.txt', 'r')
    address_book = json.load(file)
    file.close()
except:
    print("address_book.txt doesn't exist, create empty address book")


while True:
    name = input("Please enter a name (or exit to quit the program): ")
    if name == 'exit':
        break
    phone_number = int(input("Please enter the associated phone number: "))

    address_book[name] = phone_number


address_book_string = json.dumps(address_book)

file = open('address_book.txt', 'w')
file.write(address_book_string)
file.close()