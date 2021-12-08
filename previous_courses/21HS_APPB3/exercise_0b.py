# write a function called is_even that returns True if the provided number is even

# if number % 2 == 0 -> number is even


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(14))

x = 10

if is_even(x):
    print(x / 2)
else:
    print((x + 1) / 2)
