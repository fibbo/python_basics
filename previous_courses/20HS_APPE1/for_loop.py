

def is_even_or_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print('{} is even'.format(number))
        else:
            print('{} is odd'.format(number))


# numbers = list(range(10))

is_even_or_odd(list(range(10)))
print('the end')