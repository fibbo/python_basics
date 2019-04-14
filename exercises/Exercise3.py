import math


def volume_from_radius(radius):
    return 4*math.pi/3 * radius ** 3


radius = int(input('Radius: '))
print(volume_from_radius(radius))
