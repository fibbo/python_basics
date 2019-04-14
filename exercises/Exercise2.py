import math


def distance(px1, py1, pz1, px2, py2, pz2):
    '''
    Calculates the distance between 2 points
    '''
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2 + (pz2 - pz1) ** 2)

# Read from input (aka keyboard inputs)
print("Point 1 is the center of a sphere, point 2 is lies somewhere on the sphere")
print("Calculate the volume of the sphere")

x1 = int(input('Center: x-coordinate\n'))
y1 = int(input('Center: y-coordinate\n'))
z1 = int(input('Center: z-coordinate\n'))

x2 = int(input('Point 2 x-coordinate\n'))
y2 = int(input('Point 2 y-coordinate\n'))
z2 = int(input('Point 2 z-coordinate\n'))

print(distance(x1, y1, z1, x2, y2, z2))
