import math


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

p1x = int(input("Please enter x1: "))
p1y = int(input("Please enter y1: "))
p1z = int(input("Please enter z1: "))
p2x = int(input("Please enter x2: "))
p2y = int(input("Please enter y2: "))
p2z = int(input("Please enter z2: "))


distance(p1x, p1y, p1z, p2x, p2y, p2z)
