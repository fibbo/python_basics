def count_words(words, min_word_length):
    counter = 0
    for word in words:
        if len(word) >= min_word_length:
            # counter = counter + 1
            counter += 1  # ALIAS FOR: counter = counter + 1
    return counter


names = ["Philipp", "Celina", "Tom", "Tim", "Susi"]

print(count_words(names, 4))


"""
Short hand notation for simple math operation

counter = counter * 2
counter *= 2

counter = counter / 2
counter /= 2
"""
