def count_words(words, min_word_length):
    number_of_words = 0

    for word in words:
        if len(word) >= min_word_length:
            number_of_words += 1
            # number_of_words = number_of_words + 1
    print(number_of_words)


count_words(['test', 'longtest', 'a'], 2)