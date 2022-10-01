def count_words(words, min_word_length):
    counter = 0
    # match = []
    for word in words:
        if len(word) >= min_word_length:
            # match.append(word)
            counter += 1  # counter = counter + 1
    return counter
    # return match


words = ["Emanuel", "John", "Ale"]
print(count_words(words, 4))
