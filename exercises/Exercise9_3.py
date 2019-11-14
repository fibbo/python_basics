import math

def proper_round(number):
    decimal_part = number - int(number)
    if decimal_part >= 0.75:
        decimal_part = 1
    elif decimal_part >= 0.25:
        decimal_part = 0.5
    else:
        decimal_part = 0.0
    return int(number) + decimal_part 

def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return proper_round(mark)

max_points = input('Enter maximum score\n')

grade_dict = {}

while True:
    name = input('Enter the name\n')
    if name == 'exit':
        break
    points = input('Enter points\n')
    grade_dict[name] = calculate_mark(points, max_points)


for name, grade in grade_dict.items():
    print("{} has grade: {}".format(name, grade))
