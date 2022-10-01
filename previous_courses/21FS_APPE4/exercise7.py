def fizz_buzz(numbers):

    # While there is at least one element in the list -> len(list) > 0
    while len(numbers) > 0:
        value = numbers[0]
        if value % 15 == 0:
            print("FizzBuzz")
        elif value % 3 == 0:
            print("Fizz")
        elif value % 5 == 0:
            print("Buzz")
        else:
            print(value)
        # Delete the first element of the list
        del numbers[0]


numbers = list(range(31))

fizz_buzz(numbers)
