words = ["Emanuel", "John", "Ale"]
min_word_length = 4
counter = 0
for word in words:
    if len(word) >= min_word_length:
        counter += 1

print(counter)
