def multiply_by_two(value):
    result = value * 2
    return result

def divide_by_two(value):
    result = value * 2
    return result

def add_two(value):
    result = value + 2
    return result

def test(value):
    value = multiply_by_two(value)
    value = divide_by_two(value)
    value = add_two(value)
    return value


value = 16

result = test(16)

if result != 18:
    print("My code is wrong")

# value = multiply_by_two(value)
# value = divide_by_two(value)
# value = add_two(value)
# print(value)