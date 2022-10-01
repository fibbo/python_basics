import random

target_number = random.randrange(1, 101)

n_guess = 1

while True:
    guess = int(input("Please enter your guess (1-100): "))

    if guess == target_number:
        print(f"Congratulations you found the number. It took you {n_guess} tries")
        break

    if guess < target_number:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")

    n_guess += 1
