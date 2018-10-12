def print_reverse(text):
    counter = len(text)-1
    while counter >= 0:
        # end="" prevents a line break after a print
        print(text[counter], end="")
        counter -= 1


string = input('String to reverse: ')
print_reverse(string)
