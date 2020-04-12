# index = 0
# while index < len(names):
#     name = names[index]
#     print(name)
#     index = index + 1


def print_reverse(string):
    # print string in reverse
    index = len(string) - 1
    reversed_string = str()
    while index >= 0:
        # print(string[index], end='')
        reversed_string += string[index]
        # reversed_string = reversed_string + string[index]
        index = index - 1

    print(reversed_string)


print_reverse('Hello World')
