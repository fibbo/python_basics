import random

target = random.randrange(1, 101)

counter = 1
while counter < 10:
    guess = int(input("Please enter your guess: "))

    if guess > target:
        print("Your guess was too high.")
    elif guess < target:
        print("Your guess was too low.")
    else:
        print("You got it! It took you {} tries".format(counter))
        break
    counter += 1

if counter == 10:
    print("Sorry, you did not guess the correct number")
