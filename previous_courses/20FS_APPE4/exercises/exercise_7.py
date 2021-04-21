def fizz_buzz(numbers):

    while len(numbers) > 0:
        number = numbers[0]
        fizz_buzz_string = ''
        # if number % 15 == 0:
        #     print('FizzBuzz')
        # elif number % 5 == 0:
        #     print('Buzz')
        # elif number % 3 == 0:
        #     print('Fizz')
        # else:
        #     print(number)

        if number % 3 == 0:
            fizz_buzz_string = 'Fizz'
        if number % 5 == 0:
            fizz_buzz_string = fizz_buzz_string + 'Buzz'
        
        if fizz_buzz_string != '':
            print(fizz_buzz_string)
        else:
            print(number)


        del(numbers[0])
    

test_numbers = list(range(0, 5))

print(fizz_buzz(test_numbers))