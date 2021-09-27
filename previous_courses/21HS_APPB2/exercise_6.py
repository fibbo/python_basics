def count_words(words, min_word_length):
    counter = 0
    for word in words:
        if len(word) >= min_word_length:
            counter += 1
    return counter


names = ["Emanuel", "John", "Ale"]
n = 4
print(f"{names} contains {count_words(names, n)} elements with {n} characters and more")

# names_list = []
# while True:
#     name = input("Enter a name or type exit to quit and call the function: ")
#     if name == "exit":
#         break
#     names_list.append(name)

# print(count_words(names_list, 4))
