def FizzBuzz(number):
# Implicit checking for 15. Assembling the final string
    fizz_string = ""
    if number % 3 == 0:
        fizz_string = fizz_string + "Fizz"
    if number % 5 == 0:
        fizz_string = fizz_string + "Buzz"
    
    print("{}: {}".format(number, fizz_string))

# Explicit checking for 15
    # if number % 15 == 0:
    #     print("{}: {}".format(number, "FizzBuzz"))
    # elif number % 5 == 0:
    #     print("{}: {}".format(number, "Buzz"))
    # elif number % 3 == 0:
    #     print("{}: {}".format(number, "Fizz"))
    # else:
    #     print(number)

numbers_list = list(range(1, 101))

while len(numbers_list) > 0:
    fizz_string = ""
    if numbers_list[0] % 3 == 0:
        fizz_string = fizz_string + "Fizz"
    if numbers_list[0] % 5 == 0:
        fizz_string = fizz_string + "Buzz"
    
    print("{}: {}".format(numbers_list[0], fizz_string))

    #  FizzBuzz(numbers_list[0])
    del(numbers_list[0])