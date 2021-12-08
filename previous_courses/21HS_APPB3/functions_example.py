def print_two_values(value_1, value_2):
    print(value_1)
    print(value_2)
    return value_1
    print("This will never be executed")


def no_input_function():
    fav_number = input("What is your favorite number? ")
    print(f"{fav_number}? Cool, thats mine too!")


print_two_values(1, 2)
