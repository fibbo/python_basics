def compare(n1, n2):
    if n1 > n2:
        print(1)
    if n1 == n2:
        print(0)
    if n2 > n1:
        print(-1)


x = int(input("Enter value 1\n"))
y = int(input("Enter value 2\n"))
compare(x, y)
