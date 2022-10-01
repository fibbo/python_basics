import random


file = open("random_numbers.txt", "w")

for i in range(1000):
    file.write(str(random.randrange(1, 10000)) + "\n")

file.close()
