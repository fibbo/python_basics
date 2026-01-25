text = input("String to reverse: ")
index = len(text) - 1
rev_string = ""
while index >= 0:
    rev_string += text[index]
    print(text[index])
    index -= 1

print(rev_string)
