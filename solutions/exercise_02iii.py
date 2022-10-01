import math


def volume_from_points(px1, py1, pz1, px2, py2, pz2):
    radius = distance(px1, py1, pz1, px2, py2, pz2)
    return volume_from_radius(radius)


def distance(px1, py1, pz1, px2, py2, pz2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2 + (pz2 - pz1) ** 2)


def volume_from_radius(radius):
    return 4.0 / 3 * math.pi * radius**3


x1 = int(input("Center: x-coordinate: "))
y1 = int(input("Center: y-coordinate: "))
z1 = int(input("Center: z-coordinate: "))

x2 = int(input("Surface point x-coordinate: "))
y2 = int(input("Surface Point y-coordinate: "))
z2 = int(input("Surface Point z-coordinate: "))

print(volume_from_points(x1, y1, z1, x2, y2, z2))
