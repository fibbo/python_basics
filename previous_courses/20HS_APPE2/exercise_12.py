import json

def write_phonebook_to_file(phone_book, file_name):
    phone_book_string = json.dumps(phone_book)
    with open(file_name, 'w') as f:
        f.write(phone_book_string)


def read_phonebook_from_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            return json.loads(line)


phone_book = {}

phone_book = read_phonebook_from_file('address_book.txt')


while True:
    name = input('Please enter the name or type exit to quit: ')
    
    if name == 'exit':
        write_phonebook_to_file(phone_book, 'address_book.txt')
        break
    if name in phone_book:
        print(f'Name {name} already exists, you will overwrite it')
    phone_book[name] = input('Enter the phone number: ')