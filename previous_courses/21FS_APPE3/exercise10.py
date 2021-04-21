import random

target = random.randrange(1, 101)

count = 1
guess = -1

while guess != target:
  guess = int(input('Please enter your guess: '))

  if guess == target:
    print(f'You got it! It took you {count} tries')
    break

  if guess < target:
    print('Your guess was too low.')
  else:
    print('Your guess is too high.')
  
  count += 1