def compare(x, y):
    if x > y:
        print(1)
    elif x == y:
        print(0)
    elif y > x:  # else: is also fine
        print(-1)


x_value = int(input("Enter x: "))
y_value = int(input("Enter y: "))


compare(x_value, y_value)
