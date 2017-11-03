import random

random_number_to_guess = random.randrange(1, 100)

# The first guess is initialized to zero. We know that this is not equal to
# the random number, as the random number lies between 1 and 100
guessed_number = 0

counter = 1

# While the correct number has not been guessed we play
while random_number_to_guess != guessed_number:
    # Ask the user for her/his guess
    guessed_number = int(input('Guessed number: '))

    if guessed_number == random_number_to_guess:
        print('Yeah! The random number is ' + str(random_number_to_guess))
        print('It took you ' + str(counter) + ' rounds')
    elif guessed_number < random_number_to_guess:
        print('Sry, too low!')
    else:
        print('Sry, too high!')

    counter += 1
