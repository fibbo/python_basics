def reverse_string(text):
    index = len(text) - 1
    reversed_string = ""
    while index >= 0:
        # reversed_string = reversed_string + text[index]
        reversed_string += text[index]
        # index = index - 1
        index -= 1

    print(reversed_string)


reverse_string("Hello World")
