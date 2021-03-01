import random

target = int(input('Which number should the computer guess? '))

counter = 1

lower_bound = 1
upper_bound = 101

while True:
    guess = random.randrange(lower_bound, upper_bound)
    if guess == target:
        print('The computer found the number in {} tries'.format(counter))
        break
    if guess > target:
        upper_bound = guess
    elif guess < target:
        lower_bound = guess + 1

    counter += 1