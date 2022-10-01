def print_reverse(text):
    index = len(text) - 1
    reversed_string = ""
    while index >= 0:
        # print(text[index])
        # reversed_string = reversed_string + text[index]
        reversed_string += text[index]
        # index = index - 1
        index -= 1
    print(reversed_string)


def print_reverse2(text):
    index = len(text) - 1
    while index >= 0:
        print(text[index], end="")
        index -= 1


print_reverse2("Hello World")

print()

print("1234", "word", sep="*")
