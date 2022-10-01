import random
import math
import matplotlib.pyplot as plt


# target_number = int(input("Please enter your target number\n"))
def binary_guesser(guess, target_number, lower_bound, upper_bound):
    if target_number < guess:
        upper_bound = guess
        guess -= math.ceil((guess - lower_bound) / 2)
    else:
        lower_bound = guess
        guess += math.ceil((upper_bound - guess) / 2)

    return guess, lower_bound, upper_bound


def run(target_number, guesser):
    lower_bound = 1
    upper_bound = 101
    counter = 1
    guess = random.randrange(1, 101)
    while True:
        # print('Guessed number: {}'.format(guess))
        if guess == target_number:
            # print('The number is {}'.format(guess))
            # print('It took me {} rounds.'.format(counter))
            return counter
        guess, lower_bound, upper_bound = guesser(
            guess, target_number, lower_bound, upper_bound
        )
        counter += 1


averages = []
for i in range(1, 101):
    tries = []
    for _ in range(500):
        tries.append(run(i, binary_guesser))
    averages.append(sum(tries) / len(tries))

plt.plot(list(range(1, 101)), averages)
plt.savefig("average_tries_vs_target_number.png")
plt.xticks(range(1, 101, 2))
plt.show()

print(sum(averages) / len(averages))
