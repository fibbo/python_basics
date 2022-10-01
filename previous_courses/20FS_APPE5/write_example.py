def write_file(number):
    with open("test_file.txt", "a") as f:
        f.write("{}: First line in my text file\n".format(number))
        f.write("{}: Second line in my text file\n".format(number))
        f.write("{}: Third line\n".format(number))


for i in range(4):
    write_file(i)
