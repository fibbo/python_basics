data = []

with open("data.log", "r") as f:
    for line in f:
        line = line.strip()
        data.append(int(line))


print(sum(data) / len(data))
