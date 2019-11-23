def print_reverse(text):
    index = len(text) - 1
    while index >= 0:
        print(text[index])
        index = index - 1

def print_reverse2(text):
    index = 1
    while index <= len(text):
        print(text[-index])
        index = index + 1

# print_reverse("Some string")

# print_reverse2("Another string")

a_string = "Some text"
print(a_string[::-1])