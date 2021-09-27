def print_reverse(text):
    index = len(text) - 1
    reversed_string = ""
    while index >= 0:
        # print(text[-index])
        # reversed_string = reversed_string + text[-index]
        reversed_string += text[index]
        # index = index + 1
        index -= 1

    return reversed_string


# print(print_reverse("Hello"))


def print_reverse2(text):
    index = len(text) - 1

    while index >= 0:
        print(text[index], end="")
        index -= 1
    print()


# print_reverse2("Hello")

string_to_reverse = "Reverse this string"

print(string_to_reverse[::-1])
