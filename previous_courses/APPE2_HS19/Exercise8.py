def count_words(words, min_word_length):
    matches = []
    count = 0
    for word in words:
        if len(word) >= min_word_length:
            matches.append(word)
            count = count + 1
    print("Found {} words: {}".format(count, matches))


cities = ['Hamburg', 'New York', 'Zurich', 'Tokyo']

count_words(cities, 7)