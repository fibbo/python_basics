import math


def get_circle_properties(radius):
    circumeference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return (circumeference, area)


properties = get_circle_properties(2.3)

print(f'cirucmference: {properties[0]}')
print(f'area: {properties[1]}')


some_string = 'Hello World'
print(some_string[0])

some_string[1] = 'a'