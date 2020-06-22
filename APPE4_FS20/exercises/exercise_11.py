import random


target_number = int(input('Enter the target number: '))


counter = 1

lower_bound = 1
upper_bound = 101

while True:
    guess = random.randrange(lower_bound, upper_bound)

    if guess == target_number:
        print('Computer found the target number in {}'.format(counter))
        break

    if guess > target_number:
        upper_bound = guess
    else:
        lower_bound = guess + 1
    counter += 1