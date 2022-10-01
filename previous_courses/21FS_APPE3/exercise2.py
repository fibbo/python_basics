import math


def distance(x1, y1, z1, x2, y2, z2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"distance {result}")
    return result


def volume_from_radius(radius):
    result = 4 * math.pi / 3 * radius**3
    print(f"volume {result}")
    return result


def volume_from_points(x1, y1, z1, x2, y2, z2):
    radius = distance(x1, y1, z1, x2, y2, z2)
    volume = volume_from_radius(radius)
    print(volume)
    return volume


print(volume_from_points(0, 0, 0, 1, 1, 1))
