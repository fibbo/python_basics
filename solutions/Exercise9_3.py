import math

def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round_to(mark, 0.5)

max_points = input('Enter maximum score: ')

grade_dict = {}

while True:
    name = input('Enter the name: ')
    if name == 'exit':
        break
    points = input('Enter points: ')
    grade_dict[name] = calculate_mark(points, max_points)


for name, grade in grade_dict.items():
    print("{} has grade: {}".format(name, grade))
