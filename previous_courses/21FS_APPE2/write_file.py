import random

with open("my_text.txt", "w") as f:
    for _ in range(1000):
        f.write(str(random.randrange(1, 1001)) + "\n")
