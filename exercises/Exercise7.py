def print_reverse(text):
    index = len(text)-1
    rev_string = ""
    while index >= 0:
        rev_string += text[index]
        print(text[index], end="")  # end="" prevents a line break after a print
        index -= 1

    return rev_string


string = input('String to reverse: ')
print_reverse(string)
