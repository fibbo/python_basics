import random

random.seed(12)
target_number = random.randint(1, 100)

counter = 1

while True:
    guess = int(input("Enter your guess: "))
    if guess == target_number:
        break
    if guess < target_number:
        print("Guess is too low")
    else:
        print("Guess is too high")
    counter += 1

print("It took you {} guess".format(counter))
