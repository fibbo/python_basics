import random


target = random.randrange(1,101)


number_of_guesses = 1

# while True:
#     guess = int(input('Please enter your guess: '))

#     if guess == target:
#         print(f'You got it! It took you {number_of_guesses} tries')
#         break

#     if guess > target:
#         print('Your guess is too high')
#     else:
#         print('Your guess is too low')

#     number_of_guesses += 1

guess = -1

while guess != target:
    guess = int(input('Please enter your guess: '))


    if guess > target:
        print('Your guess is too high')
    elif guess < target:
        print('Your guess is too low')

    if guess == target:
        print(f'You got it! It took you {number_of_guesses} tries')

    number_of_guesses += 1