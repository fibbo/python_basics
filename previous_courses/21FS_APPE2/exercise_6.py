def print_reverse(text):
  reversed_string = ''
  index = len(text) - 1
  while index >= 0:
    # print(text[index])
    # reversed_string = reversed_string + text[index]
    reversed_string += text[index]
    # index = index - 1
    index -= 1
  print(reversed_string)


print_reverse("Hello World")

# print("Hello World"[::-1])