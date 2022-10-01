import random


target_number = random.randrange(1, 101)

counter = 1
while True:
    guess = int(input("Please enter your guess: "))

    if guess == target_number:
        print(
            "Congratulations, you found the number, it took you {} tries".format(
                counter
            )
        )
        break

    if guess < target_number:
        print("Guess was too low")
    else:
        print("Guess was too high")

    counter += 1
