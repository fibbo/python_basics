import math
from math import radians
a_tuple = (1, 2, 3, 'asdf', True)


print(a_tuple)

print(a_tuple[0])
print(a_tuple[-1])
# print(a_tuple[len(a_tuple)])

# a_tuple[0] = 2

# a_string = "Hello World"
# a_string[0] = "J"


def circle_properties(radius):
    area = math.pi*radius
    circumeference = 2*math.pi*radius
    return (area, circumeference)


circle_prop = circle_properties(3.0)

print(circle_prop[0])