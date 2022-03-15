def is_between(n1, n2, n3):
    return n1 <= n2 <= n3


x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(is_between(x, y, z))
