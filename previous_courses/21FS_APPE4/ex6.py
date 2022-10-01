# list_a = 'hello'


def reverse(text):
    index2 = 1
    while index2 <= len(text):
        print(text[-index2], end="")
        index2 = index2 + 1
    print()


def reverse2(text):
    index2 = 1
    reversed_string = ""
    while index2 <= len(text):
        # reversed_string = reversed_string + text[-index2]
        reversed_string += text[-index2]
        index2 = index2 + 1

    print(reversed_string)


reverse("Hello World")
reverse2("Hello World")
