numbers = list(range(1000000))

for number in numbers:
    if number == 1000:
        break
    print(number)

while True:
    answer = input('Do you like python? ')
    if answer == 'yes':
        break
    else:
        print('wrong answer')


