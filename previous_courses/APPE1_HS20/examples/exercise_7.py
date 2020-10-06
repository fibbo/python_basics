def fizz_buzz(numbers):
    while len(numbers) > 0:
        first_number = numbers[0]

        answer_string = ''
        if first_number % 3 == 0:
            answer_string = answer_string + 'Fizz'
        if first_number % 5 == 0:
            answer_string = answer_string + 'Buzz'
        if len(answer_string) > 0:
            print(answer_string)
        else:
            print(first_number)

        ## Possible solution 2
        # if first_number % 15 == 0:
        #     print('FizzBuzz')
        # elif first_number % 3 == 0:
        #     print('Fizz')
        # elif first_number % 5 == 0:
        #     print('Buzz')
        # else:
            # print(first_number)

        del(numbers[0])
        


fizz_buzz(list(range(1,101)))