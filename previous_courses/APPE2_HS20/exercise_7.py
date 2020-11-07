def FizzBuzz(numbers):

    while len(numbers) > 0:
        number = numbers[0]
        output = ''
        if number % 3 == 0:
            output += 'Fizz'
        if number % 5 == 0:
            output += 'Buzz'
        if output != '':
            print(number, output)
        else:
            print(number)

        del(numbers[0])


def FizzBuzz2(numbers):
    while len(numbers) > 0:
        number = numbers[0]
        if number % 15 == 0:
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)

        del(numbers[0])

FizzBuzz2(list(range(101)))