import math
import random


target = int(input("Please enter target number (from 1 to 100): "))


number_of_guesses = 1

lower_bound = 1
upper_bound = 100
random.seed(0)
guess = random.randrange(1, 101)

while True:

    if guess == target:
        print(f"The computer got it in {number_of_guesses} tries")
        break

    if guess > target:
        upper_bound = guess - 1
        guess -= math.ceil((guess - lower_bound) / 2)
    else:
        lower_bound = guess + 1
        guess += math.ceil((upper_bound - guess) / 2)

    number_of_guesses += 1
