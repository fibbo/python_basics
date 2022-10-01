contents = []

with open("my_text.txt", "r") as f:
    for line in f:
        line = line.strip()
        contents.append(int(line))


# print(contents)

print("The average of the random numbers is {}".format(sum(contents) / len(contents)))
