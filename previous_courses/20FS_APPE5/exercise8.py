def count_words(words, min_word_length):
    counter = 0
    matched_words = []
    for word in words:
        if len(word) >= min_word_length:
            counter += 1
            matched_words.append(word)

    return counter, matched_words


names = ['Tom', 'Celina', 'Philipp', 'Maria', 'Ale']

result = count_words(names, 5)

print('I found {} words that matched the criteria'.format(result[0]))
print('Words that matched the criteria: ')
for word in result[1]:
    print(word)

