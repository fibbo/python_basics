import random

target = int(input("Please enter the number to guess: "))


count = 1

lower_bound = 1
upper_bound = 101

while True:
    guess = random.randrange(1, 101)

    if guess == target:
        print(f"That guess was correct. It took {count} tries.")
        break

    # Improve algorithm
    # Depending whether the guess was too low or too high
    # adjust the respective bound

    count += 1
