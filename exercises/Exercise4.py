import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y        

def volume_from_points(px1, py1, px2, py2):
    radius = distance(px1, py1, px2, py1)
    return volume_from_radius(radius)


def volume_from_points2(p1: Point, p2: Point):
    radius = distance2(p1, p2)
    return volume_from_radius(radius)


def distance2(p1: Point, p2: Point):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def distance(px1, py1, px2, py2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)


def volume_from_radius(radius):
    return 4.0/3 * math.pi * radius**3


x1 = int(input('Point 1 x-cord: '))
y1 = int(input('Point 1 y-cord: '))
x2 = int(input('Point 2 x-cord: '))
y2 = int(input('Point 2 y-cord: '))

print(volume_from_points(x1, y1, x2, y2))
