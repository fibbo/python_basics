def fizz_buzz(numbers):
    while len(numbers) > 0:
        n = numbers[0]
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0:
            print('Fizz')
        else:
            print(n)
        
        del numbers[0]

def fizz_buzz2(numbers):
    while len(numbers) > 0:
        n = numbers[0]
        result_string = ''
        if n % 3 == 0:
            result_string += 'Fizz'
        if n % 5 == 0:
            result_string += 'Buzz'
        if len(result_string) > 0:
            print(result_string)
        else:
            print(n)
        del numbers[0]


def fizz_buzz3(numbers, backwards=False):
    if backwards:
        index = -1
    else:
        index = 0
    while len(numbers) > 0:
        n = numbers[index]
        result_string = ''
        if n % 3 == 0:
            result_string += 'Fizz'
        if n % 5 == 0:
            result_string += 'Buzz'
        if len(result_string) > 0:
            print(result_string)
        else:
            print(n)
        del numbers[index]


fizz_buzz3(list(range(101)), True)
        