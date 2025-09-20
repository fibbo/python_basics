def print_reverse(text):
    """
    The function implements two solution at the same time:
        rev_string will be assembled while the iteration is happening and returned at the end of the function.
        At the same time print with end="" is specified prints characters as they are iterated.
    """
    index = len(text) - 1
    rev_string = ""
    while index >= 0:
        rev_string += text[index]
        print(text[index])
        index -= 1

    return rev_string


string = input("String to reverse: ")
print_reverse(string)
