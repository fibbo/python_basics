import math
import random


def main():
    lower_bound = 1
    upper_bound = 101
    counter = 1

    target_number = int(input("Please enter your target number: "))

    guess = random.randrange(lower_bound, upper_bound)

    while True:
        print(f"Guessed number: {guess}")
        if guess == target_number:
            print(f"The number is {guess}")
            print(f"It took me {counter} rounds.")
            break
        if target_number < guess:
            upper_bound = guess
            guess -= math.ceil((guess - lower_bound) / 2)
        else:
            lower_bound = guess
            guess += math.ceil((upper_bound - guess) / 2)
        counter += 1


main()
