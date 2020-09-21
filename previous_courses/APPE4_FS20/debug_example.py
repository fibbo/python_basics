def add_two(value):
    result = value + 2
    return result

def multiply_by_two(value):
    result = value * 2
    return result

def divide_by_two(value):
    result = value / 2
    return result


value = int(input("Enter a value: "))
value = add_two(value)
value = multiply_by_two(value)
value = divide_by_two(value)
print(value)