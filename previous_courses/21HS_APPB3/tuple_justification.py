import math


def get_circle_properties(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    return circumference, area, radius


circle_prop = get_circle_properties(1.0)

print(circle_prop[::-1])

circle_prop[0] = True

print(circle_prop)
