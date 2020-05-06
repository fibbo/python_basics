def fizz_buzz(numbers):
    index = 0
    while index < len(numbers):
        output = ''
        if numbers[index] % 3 == 0:
            output += 'Fizz'
        if numbers[index] % 5 == 0:
            output += 'Buzz'
        if output != '':
            print(output)
        else:
            print(numbers[index])
        index += 1


numbers = list(range(101))
fizz_buzz(numbers)