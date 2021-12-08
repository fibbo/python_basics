def reverse_string(text):
    reversed_string = ""
    index = len(text) - 1
    while index >= 0:
        reversed_string += text[index]
        # print(name)
        # index = index - 1
        index -= 1
    print(reversed_string)


reverse_string("Hello World")


# value = 0
# value += 2 # value = value + 2
# value *= 3 # value = value * 3
# value /= 1.5 # value = value / 1.5
# print(value)
