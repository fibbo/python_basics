import random

lower_bound = 1
upper_bound = 101
counter = 1

target_number = int(input("Please enter your target number\n"))

guess = random.randrange(1, 101)
while True:
    print('Guessed number: {}'.format(guess))
    if guess == target_number:
        print('The number is {}'.format(guess))
        print('It took me {} rounds.'.format(counter))
        break
    elif target_number < guess:
        upper_bound = guess
        guess -= int((guess - lower_bound)/2)
    else:
        lower_bound = guess
        guess += int((upper_bound - guess)/2)
    counter += 1
