import random


target_number = 50  # int(input('Please enter target number: '))

n_guess = 1
lower_bound = 1
upper_bound = 101
while True:
    guess = random.randrange(lower_bound, upper_bound)
    if guess == target_number:
        print(f"Congratulations you found the number. It took you {n_guess} tries")
        break

    if guess > target_number:
        upper_bound = guess
    else:
        lower_bound = guess + 1
    n_guess += 1
