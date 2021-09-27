with open("test.txt", "r") as f:
    for line in f:
        line = line.strip()
        split_line = line.split()
        print(split_line)


with open("numbers.txt", "r") as f:
    for line in f:
        split_line = line.split()
        numbers = []
        for n in split_line:
            numbers.append(int(n))

        print(f"Sum of all the numbers is {sum(numbers)}")
