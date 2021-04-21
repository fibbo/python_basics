def compare(x, y):
    if x > y:
        print(1)
    elif y > x:
        print(-1)
    else:
        print(0)


x_input = int(input('Please enter a number for x: '))
y_input = int(input('Please enter a number for y: '))

compare(x_input, y_input)
