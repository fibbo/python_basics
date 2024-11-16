import math


def distance(px1, py1, pz1, px2, py2, pz2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2 + (pz2 - pz1) ** 2)


# Read from input (aka keyboard inputs)
print("Point 1 is the center of a sphere, point 2 is lies somewhere on the sphere")
print("Calculate the volume of the sphere")

x1 = int(input("Center: x-coordinate: "))
y1 = int(input("Center: y-coordinate: "))
z1 = int(input("Center: z-coordinate: "))

x2 = int(input("Surface point x-coordinate: "))
y2 = int(input("Surface Point y-coordinate: "))
z2 = int(input("Surface Point z-coordinate: "))

print(distance(x1, y1, z1, x2, y2, z2))
