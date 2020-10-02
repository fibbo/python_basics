import math

def area(radius):
    area = math.pi * radius ** 2
    return area


total_area = 0
total_area = total_area + area(4)
total_area = total_area + area(3)

area_lake = 43

print('the ratio of lake covered by lilies is {}'.format(area_lake / total_area))
