import random


# target = int(input("Enter the target number for the computer to guess: "))
target = 23
counter = 1

lower_bound = 1
upper_bound = 101
while True:
    random_guess = random.randrange(lower_bound, upper_bound)
    if random_guess == target:
        print("Found the number!")
        print("It took {} tries".format(counter))
        break
    if random_guess > target:
        upper_bound = random_guess
    else: #random_guess < target
        lower_bound = random_guess + 1

    counter += 1