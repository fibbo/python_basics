import random

def play_game():
    lower_bound = 1
    upper_bound = 101

    counter = 1
    while True:
        guess = random.randrange(lower_bound, upper_bound)
        print(f'I guessed {guess}')

        feedback = input('< too low, > too high, = correct ')

        if feedback == '<':
            lower_bound = guess + 1
        if feedback == '>':
            upper_bound = guess
        else:
            print(f'I got it! It took me {counter} tries')
            break
        counter += 1


play_game()