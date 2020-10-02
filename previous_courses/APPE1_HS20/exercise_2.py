import math


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def volume_from_radius(radius):
    return 4 * math.pi / 3 * radius ** 3


def volume_from_points(x1, y1, z1, x2, y2, z2):
    radius = distance(x1, x1, z1, x2, y2, z2)
    volume = volume_from_radius(radius)
    return radius, volume

print(volume_from_points(1, 1, 1, 0, 0, 0))

volume, radius = volume_from_points(1, 1, 1, 0, 0, 0)

results = volume_from_points(1,1,1,0,0,0)

print(results[0])
print(results[1])

results[0] = 0