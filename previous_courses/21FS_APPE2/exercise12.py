import json

address_book = {}

with open("address_book.txt", "r") as f:
    address_book = json.load(f)

while True:
    name = input("Please enter the name or type exit to quit: ")
    if name == "exit":
        break

    phone_number = input("Please enter the phone number: ")
    address_book[name] = phone_number

with open("address_book.txt", "w") as f:
    address_book_json = json.dumps(address_book)
    f.write(address_book_json)
