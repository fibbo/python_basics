def sequence(n):
    max_number = 0
    while n != 1:
        print(n)
        if n > max_number:
            max_number = n
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    print(f"The highest number in the sequence was: {max_number}")


sequence(129)
