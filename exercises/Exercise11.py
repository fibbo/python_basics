lower_bound = 1
upper_bound = 100
counter = 1

while True:
    guessed_number = int((lower_bound + upper_bound) / 2)
    print('Guessed number: ' + str(guessed_number))
    answer = input("Answer: ")
    if answer == '=':
        print('The number is ' + str(guessed_number))
        print('It took me ' + str(counter) + ' rounds.')
        break
    elif answer == '<':
        lower_bound = guessed_number + 1
    else:
        upper_bound = guessed_number - 1
    counter += 1
