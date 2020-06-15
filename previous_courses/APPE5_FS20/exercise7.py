def fizz_buzz(numbers):
    index = 0
    while index < len(numbers):
        output = ''
        if numbers[index] % 3 == 0:
            output += 'Fizz'
        if numbers[index] % 5 == 0:
            output += 'Buzz'

        if output == '':
            print(numbers[index])
        else:
            print(output)

        index += 1


fizz_buzz(list(range(1, 101)))