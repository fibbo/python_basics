def print_reverse(text):
    counter = len(text)-1
    while counter >= 0:
        print(text[counter])
        counter -= 1

string = input('String: ')
print_reverse(string)