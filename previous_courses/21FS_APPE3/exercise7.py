def fizz_buzz(numbers):
    while len(numbers) > 0:
        n = numbers[0]

        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
        del numbers[0]


list_of_numbers = list(range(20))

fizz_buzz(list_of_numbers)
