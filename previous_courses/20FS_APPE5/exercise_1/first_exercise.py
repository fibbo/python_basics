def compare(x, y):
    if x > y:
        print(1)
    elif x == y:
        print(0)
    else:
        print(-1)


x_input = float(input("Please enter the first value: "))
y_input = float(input("Please enter the second value: "))

compare(x_input, y_input)
