def count_words(words_, min_word_length):
    words_over_length = 0
    for w in words_:
        if len(w) >= min_word_length:
            # w += words_over_length
            words_over_length += 1
        # value_x = len(words_over_length)+1
    # print(value_x)
    print(words_over_length)


words_ = ["Tom", "Anna", "Christopher"]
count_words(words_, 4)
