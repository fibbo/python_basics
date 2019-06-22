def count_words(words, min_word_length):
    result = 0
    for word in words:  # loop through all the words in the list
        # if length of word is greater or equal min_word_length we
        # should add it to the result
        if len(word) >= min_word_length:
            result = result + 1
    return result  # number of words found that met the criteria


word_list = ['Philipp', 'Celina', 'Tom', 'Peter', 'Maria', 'Ale']

print(count_words(word_list, 4))
