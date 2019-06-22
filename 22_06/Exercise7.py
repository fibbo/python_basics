def print_reverse(text):
    index = len(text) - 1
    while index >= 0:
        print(text[index])
        index = index - 1

print_reverse('Hello World')

print_reverse2('Hello World')
