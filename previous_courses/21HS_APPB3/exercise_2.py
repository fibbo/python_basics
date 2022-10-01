import math

# We have two points (x1, y1, z1) and (x2, y2, z2)
# where one point is the center of a sphere and
# the second point lies on the sphere. We calculate
# the distance between these two points
def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def volume_from_radius(radius):
    volume = 4 * math.pi / 3 * radius**3
    return volume


def volume_from_points(x1, y1, z1, x2, y2, z2):
    radius = distance(x1, y1, z1, x2, y2, z2)
    volume = volume_from_radius(radius)
    return volume


print(distance(0, 0, 0, 1, 1, 1))
