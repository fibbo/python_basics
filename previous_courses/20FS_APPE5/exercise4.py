import math

# From exercise 3
def volume_from_radius(radius):
    volume = 4 * math.pi / 3 * radius**3
    return volume


# From exercise 2
def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    # dx = x2 - x1
    # dy = y2 - y1
    # dz = z2 - z1
    # dx2 = dx ** 2
    # dy2 = dy ** 2
    # dz2 = dz ** 2
    # sum_of_components = dx2 + dy2 + dz2
    # result = math.sqrt(sum_of_components)
    # return result


# This is exercise 4
def volume_from_points(x1, y1, z1, x2, y2, z2):
    radius = distance(x1, y1, z1, x2, y2, z2)
    return volume_from_radius(radius)


p1x = float(input("Please enter x1: "))
p1y = float(input("Please enter y1: "))
p1z = float(input("Please enter z1: "))
p2x = float(input("Please enter x2: "))
p2y = float(input("Please enter y2: "))
p2z = float(input("Please enter z2: "))

print(volume_from_points(p1x, p1y, p1z, p2x, p2y, p2z))
