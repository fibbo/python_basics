# with open('a_text_file.txt', 'w') as text_file:
#     text_file.write('This is some text ')
#     text_file.write('this is some more text, it\'s on the same line\n')
#     text_file.write('\n \nlast line of the script that I write\n')


import random

numbers = [ random.randrange(1000) for _ in range(1000) ]

with open('input.data', 'w') as file:
    for number in numbers:
        file.write(f'{number}\n')

    # Also possible using list comprehension
    # file.writelines('\n'.join([ str(number) for number in numbers]))