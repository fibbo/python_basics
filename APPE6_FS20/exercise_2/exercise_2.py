import math

def distance(x1, y1, z1, x2, y2, z2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta_z = z2 - z1
    delta_x2 = delta_x ** 2
    delta_y2 = delta_y ** 2
    delta_z2 = delta_z ** 2
    sum_of_deltas = delta_x2 + delta_y2 + delta_z2
    distance = math.sqrt(sum_of_deltas)
    return distance

def distance2(x1, y1, z1, x2, y2, z2):
    # Calculate distance between two 3D points
    return math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


# Solution exercise 3
def volume_from_radius(radius):
    res = 4 * math.pi / 3 * radius ** 3
    print(res)
    return res


def volume_from_points(x1, y1, z1, x2, y2, z2):
    radius = distance(x1, y1, z1, x2, y2, z2)
    volume = volume_from_radius(radius)
    return volume


print(volume_from_points(0, 0, 0, 1, 1, 1))