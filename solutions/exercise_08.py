import random

random_number = random.randrange(1, 100)

counter = 1

while True:
    guess = int(input("Please enter your guess: "))
    if guess == random_number:
        print("You found the number!: ")
        print("It tooks you {} tries".format(counter))
        break
    elif guess > random_number:
        print("Too high")
    else:
        print("Too low")
    counter += 1
