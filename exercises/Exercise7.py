def print_reverse(text):
    counter = len(text)-1
    rev_string = ""
    while counter >= 0:
        rev_string += text[counter]
        print(text[counter], end="") # end="" prevents a line break after a print
        counter -= 1

    return rev_string


# string = input('String to reverse: ')
print_reverse("asdfasdf")

print(print_reverse("test"))