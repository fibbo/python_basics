import math


def volume_from_points(px1, py1, pz1, px2, py2, pz2):
    radius = distance(px1, py1, pz1, px2, py2, pz2)
    return volume_from_radius(radius)


def distance(px1, py1, pz1, px2, py2, pz2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2 + (pz2 - pz1) ** 2)


def volume_from_radius(radius):
    return 4.0 / 3 * math.pi * radius ** 3


x1 = int(input("Point 1 x-cord: "))
y1 = int(input("Point 1 y-cord: "))
z1 = int(input("Point 1 z-cord: "))
x2 = int(input("Point 2 x-cord: "))
y2 = int(input("Point 2 y-cord: "))
z2 = int(input("Point 2 z-cord: "))

print(volume_from_points(x1, y1, z1, x2, y2, z2))
