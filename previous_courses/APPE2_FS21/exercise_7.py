def fizz_buzz(numbers):
  while len(numbers) > 0:
    value = numbers[0]

    # if value % 15 == 0:
    #   print('FizzBuzz')
    # elif value % 3 == 0:
    #   print('Fizz')
    # elif value % 5 == 0:
    #   print('Buzz')
    # else:
    #   print(value)

    output_string = ''

    if value % 3 == 0:
      output_string += 'Fizz'
    if value % 5 == 0:
      output_string += 'Buzz'
    
    if len(output_string) > 0:
      print(output_string)
    else:
      print(value)
      
    del(numbers[0])


numbers = list(range(0, 101))

fizz_buzz(numbers)