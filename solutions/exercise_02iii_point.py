import math


class Point3D(object):
    # when creating a point we can either pass the coordinates
    # or just create a new point without any coordinates and they
    # will be set to 0
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # defining a __str__ function we can control the behaviour when
    # we call print on our Point3D objects
    def __str__(self):
        return "x: {} \t y: {} \t z: {}".format(self.x, self.y, self.z)


def volume_from_points(p1, p2):
    radius = distance(p1, p2)
    return volume_from_radius(radius)


def distance(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)


def volume_from_radius(radius):
    return 4.0 / 3 * math.pi * radius ** 3


x1 = int(input("Point 1 x-coordinate: "))
y1 = int(input("Point 1 y-coordinate: "))
z1 = int(input("Point 1 z-coordinate: "))
x2 = int(input("Point 2 x-coordinate: "))
y2 = int(input("Point 2 y-coordinate: "))
z2 = int(input("Point 2 z-coordinate: "))

p1 = Point3D(x1, y1, z1)
p2 = Point3D(x2, y2, z2)

print(volume_from_points(p1, p2))
