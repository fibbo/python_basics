import random

target_number = random.randrange(1, 101)

number_of_guesses = 1

while True:
    guess = int(input("Enter your guess: "))

    if guess == target_number:
        print(f"Congrats, you found the number, it took you {number_of_guesses} tries")
        break
    if guess > target_number:
        print("You guessed to high")
    else:
        print("You guessed to low")

    number_of_guesses += 1
