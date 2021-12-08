def compare(x, y):
    if x > y:
        print(1)
    elif x < y:
        print(-1)
    else:
        print(0)


number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))

compare(number_1, number_2)
