# def count_words(words, min_word_length):
#   pass


# def calculate_mean(numbers):
#   sum_of_numbers = 0
#   for number in numbers:
#     sum_of_numbers += number
#   mean = sum_of_numbers/len(numbers)
#   return mean

# list_of_numbers = list(range(100))
# calculate_mean(list_of_numbers)

cities = ["Paris", "New York"]

word_lengths = [len(city) for city in cities if len(city) > 5]

print(word_lengths)
