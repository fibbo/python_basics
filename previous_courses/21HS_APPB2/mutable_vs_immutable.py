import math


def get_circle_data(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return (area, circumference)


a, c = get_circle_data(1)
circle_info = get_circle_data(1)
a = 2.3
print(circle_info)

print(f"The sum of the area and circumference is {circle_info[0] + circle_info[1]}")
