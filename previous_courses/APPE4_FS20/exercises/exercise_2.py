import math

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def volume_from_radius(radius):
    volume = 4 * math.pi / 3 * radius ** 3
    return volume

def volume_from_points(x1, y1, z1, x2, y2, z2):
    r = distance(x1, y1, z1, x2, y2, z2)
    v = volume_from_radius(r)
    return v

x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))

print(volume_from_points(x1, y1, z1, x2, y2, z2))