def print_reverse(text):
    index = len(text) - 1
    rev_string = ""
    while index >= 0:
        rev_string += text[index]
        # end="" prevents a line break after a print
        print(text[index], end="")
        index -= 1

    return rev_string


string = input("String to reverse: ")
print_reverse(string)
