import math

def area_of_circle(radius):
  area = math.pi * radius ** 2
  return round(area, 2)

calculated_area = area_of_circle(3)

print(calculated_area)