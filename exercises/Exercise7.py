def print_reverse(text):
    counter = len(text)-1
    while counter >= 0:
        print(text[counter], end="") # end="" prevents a line break after a print
        counter -= 1


string = input('String to reverse: ')
print_reverse(string)