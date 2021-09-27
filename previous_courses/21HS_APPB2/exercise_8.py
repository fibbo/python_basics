import random

random.seed(0)
target_number = random.randrange(1, 101)

counter = 1

while True:
    guess = int(input("Please enter your guess: "))
    if guess == target_number:
        print(f"Congratulations, you guessed correctly. It took you {counter} tries.")
        break

    counter += 1
    if guess > target_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low.")
