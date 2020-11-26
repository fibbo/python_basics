import random


def play_game():
    target = random.randrange(1, 101)

    counter = 1

    while True:
        guess = int(input('Please guess the number: '))
        if guess == target:
            print(f'Great job, it took you {counter} tries')
            break

        if guess < target:
            print('Guess higher')
        elif guess > target:
            print('Guess lower')
        
        counter += 1

while True:
    play_game()
    if input('Want to play again? ') != 'yes':
        break