def count_words(word_list, min_word_length):
    counter = 0
    for word in word_list:
        if len(word) >= min_word_length:
            counter = counter + 1
    return counter


words = ["Hello", "New York", "Alexander"]

print(count_words(words, 6))
