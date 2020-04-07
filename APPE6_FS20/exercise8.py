def count_words(words, min_word_length):
    count = 0
    for word in words:
        if len(word) >= min_word_length:
            count += 1
            # count = count + 1
    return count



names = ['Philipp', 'Anna', 'Tom', 'Stu']

print(count_words(names, 4))