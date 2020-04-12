def square(number):
    squared_number = number ** 2
    return squared_number


def square_without_return(number):
    squared_number = number ** 2
    print(squared_number)


print(square(3))
print(square_without_return(4))
