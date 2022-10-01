import random


def RunGame():
    target = random.randrange(1, 101)

    counter = 0

    while True:
        counter += 1
        guess = float(input("Enter your guess: "))
        if guess > target:
            print("Your guess is too high.")
        elif guess < target:
            print("Your guess is too low")
        else:
            print("You got it! It took you {} tries".format(counter))
            break


RunGame()

while True:
    answer = input("Do you want to play again? ")
    if answer == "yes":
        RunGame()
    else:
        break
