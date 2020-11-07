import math
from math import dist

# Exercise 2
def distance(x1, y1, z1, x2, y2, z2):
    # calculate distance between point 1 and two
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    dx2 = dx**2
    dy2 = dy**2
    dz2 = dz**2
    distance = math.sqrt( dx2 + dy2 + dz2 )
    return distance
    # return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 )

# Exercise 3
def volume_from_radius(radius):
    volume = 4 * math.pi / 3 * radius ** 3
    return volume
    # return 4 * math.pi / 3 ** radius ** 3


# Exercise 4
def volume_from_points(x1, y1, z1, x2, y2, z2):
    radius = distance(x1, y1, z1, x2, y2, z2)
    volume = volume_from_radius(radius)
    return volume


# print(distance(0, 0, 0, 1, 1, 1))

print(volume_from_points(0, 0, 0, 0, 0, 0))