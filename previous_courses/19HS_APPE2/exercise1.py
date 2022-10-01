def compare(x, y):
    if x > y:
        print(1)
    elif y > x:
        print(-1)
    else:
        print(0)


first_number = input("Please enter first number: ")
second_number = input("Please enter second number: ")

compare(first_number, second_number)
