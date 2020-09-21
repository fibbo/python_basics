def print_reverse(text):
    index = len(text) - 1
    # reversed_string = ''
    while index >= 0:
        print(text[index], end='')
        # reversed_string = reversed_string + text[index]
        index = index - 1

    # print(reversed_string)

print_reverse("Some test string")
print()
string = "Some test string2"

print(string[::-1])