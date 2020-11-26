def count_words(words, min_word_length):
    count = 0
    for word in words:
        if len(word) >= min_word_length:
            count += 1
    return count


names = ['Emanuel', 'Peter', 'Philipp', 'Ana']

print(count_words(names, 6))
