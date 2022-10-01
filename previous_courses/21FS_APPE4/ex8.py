def count_words(words, min_word_length):
    counter = 0
    for word in words:
        if len(word) >= min_word_length:
            counter += 1  # This is equal to: counter = counter + 1
    print(counter)


names = ["Emanuel", "John", "Ale"]
count_words(names, 4)
