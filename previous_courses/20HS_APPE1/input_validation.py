def read_number():
    while True:
        n = input("Please enter a number: ")
        try:
            if not ("." in n):
                return int(n)
            else:
                return float(n)
        except ValueError:
            print("Enter a valid number. {} is not a valid number.".format(n))


x = read_number()

print(x)
print(type(x))
