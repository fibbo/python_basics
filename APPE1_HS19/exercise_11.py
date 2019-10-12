import random
import math

target = int(input("Please enter the number the computer has to guess: "))

counter = 1
lower_bound = 1
upper_bound = 101

guess = random.randrange(lower_bound, upper_bound)

while True:
    print(guess)
    if guess == target:
        print("Found the target in {} tries".format(counter))
        break
    elif guess > target:
        upper_bound = guess
        guess -= math.ceil((upper_bound - lower_bound) / 2 )
    else:
        lower_bound = guess
        guess += math.ceil((upper_bound - lower_bound) / 2 )
    counter += 1