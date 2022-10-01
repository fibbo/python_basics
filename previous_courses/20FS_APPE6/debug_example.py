"""
Example to show a simple debug sessions

"""


def add_two(number):
    res = number + 2
    return res


def multiply_by_two(number):
    res = number * 3  # Error in this line
    return res


def divide_by_two(number):
    res = number / 2
    return res


start_number = 10
result = add_two(start_number)
result = multiply_by_two(result)
result = divide_by_two(result)

print(result)
