from pathlib import Path
import json

address_book_dict = {}
while True:
    name = input("Enter name or type exit to quit: ")
    if name == "exit":
        break
    phone = input("Phone: ")
    address_book_dict[name] = phone

address_book = Path("address_book.txt")
with address_book.open("w") as address_book_file:
    json.dump(address_book_dict, address_book_file)
