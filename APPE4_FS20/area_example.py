import math

def area(radius):
  result = math.pi * radius ** 2
  # print(result)
  return result

radii = [3, 4, 5, 6, 7]

sum_of_area = 0
for radius in radii:
  sum_of_area += area(radius)

print(sum_of_area / len(radii))
