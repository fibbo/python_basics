import random
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def volume_from_radius(radius):
    return 4/3*math.pi*radius**3


def volume_from_distance(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y2)
    volume = volume_from_radius(radius)
    return volume


# generating a list containing lists as elements
parent_list = list()
for x in range(20):
    sub_list = []
    for y in range(4):
        sub_list.append(random.random()*10-5)
    parent_list.append(sub_list)

# # Example with "list comprehension"
# for x in range(20):
#     parent_list.append([random.random()*10-5 for x in range(4) ])

for points in parent_list:
    print(volume_from_distance(points[0], points[1], points[2], points[3]))
