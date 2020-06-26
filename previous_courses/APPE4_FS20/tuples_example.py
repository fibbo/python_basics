import math

def get_circle_info(radius):
    area = math.pi * radius**2
    circumeference = 2 * math.pi * radius
    return (area, circumeference)


radius = 6.3

(a, c) = get_circle_info(radius)
info = get_circle_info(radius)

print(a)
print(c)

print(info[0])
print(info[1])

# info[0] = 0


name = 'Monty'