def reverse_string(text):
    index = len(text) - 1
    reversed_string = ""
    while index >= 0:
        letter = text[index]
        # reversed_string = reversed_string + letter
        reversed_string += (
            letter  # this line is equivalent to the line above, just less typing
        )
        # print(letter, end='')
        index = index - 1
    print(reversed_string)


reverse_string("Hello World")


# factor = 4
# factor = factor * 2
# factor *= 2

# division = 16
# division = division / 2
# division /= 2
