import math


def volume_from_points(px1, py1, px2, py2):
    radius = distance(px1, py1, px2, py1)
    return volume_from_radius(radius)


def distance(px1, py1, px2, py2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)


def volume_from_radius(radius):
    return 4.0/3 * math.pi * radius**3


x1 = int(input('Point 1 x-cord: '))
y1 = int(input('Point 1 y-cord: '))
x2 = int(input('Point 2 x-cord: '))
y2 = int(input('Point 2 y-cord: '))

print(volume_from_points(x1, y1, x2, y2))