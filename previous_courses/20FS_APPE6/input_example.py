answer = None

while True:
    try:
        answer = int(input("Please enter a number: "))
        break
    except ValueError:
        print("incorrect input")


# Now we got an input that is an int
print("{} was an integer".format(answer))
