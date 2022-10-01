def compare(n1, n2):
    if n1 > n2:
        print(1)
    elif n1 == n2:
        print(0)
    else:
        print(-1)


with open("custom_exercises/numbers.txt") as f:
    data = f.read().split("\n")
    for line in data:
        split_line = line.split()
        compare(int(split_line[0]), int(split_line[1]))
