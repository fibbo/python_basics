import random


target = random.randrange(1, 101)

counter = 1
# now write a while loop that allows
# guessing the number
while True:
    guess = int(input("Your guess: "))
    if guess == target:
        print("Hooray, you got it")
        print("It took you {} tries".format(counter))
        break
    if guess < target:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    counter += 1
    
