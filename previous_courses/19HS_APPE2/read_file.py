with open("my_file.txt", "r") as file:
    for line in file:
        line = line.strip()
        print(line)
