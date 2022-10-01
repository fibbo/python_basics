def collatz_conjecture(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n /= 2  # equal to n = n / 2
        else:
            n = n * 3 + 1


collatz_conjecture(13)
