import json

address_book = {}

try:
    with open("address_book.txt", "r") as address_book_file:
        address_book = json.load(address_book_file)
except FileNotFoundError:
    print("address_book.txt does not exist")


def insert_person():
    name = input("Please enter a name: ")
    phone_number = input("Please enter a phone number: ")
    address_book[name] = phone_number


def search_person():
    name = input("Please provide the name of the person: ")
    if name in address_book:
        print("The phone number of {} is: {} ".format(name, address_book[name]))
    else:
        print("Person not found")


def remove_person():
    name = input("Please provide the name of the person you want to remove: ")
    if name in address_book:
        del address_book[name]
        print("Successfully removed " + name)
    else:
        print("Person not found")


print("What do you want to do?")
print("Enter 'add' to add a new person to the address book")
print("Enter 'search' to lookup a phone number")
print("Enter 'remove' to remove a person from the address book")
print("Enter 'exit' to quit")

while True:
    action = input(">>> ")
    if action == "add":
        insert_person()
    elif action == "search":
        search_person()
    elif action == "remove":
        remove_person()
    elif action == "exit":
        break

print("Bye Bye")

with open("address_book.txt", "w") as address_book_file:
    address_book_file.write(json.dumps(address_book))
