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

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'id: {} \t name: {}'.format(self.id, self.name)

id = 0

max_points = input('Enter maximum score\n')

grade_dict = {}

while True:
    name = input('Enter the name\n')
    if name == 'exit':
        break
    student = Student(id, name)
    id += 1
    points = input('Enter points\n')
    grade_dict[student] = calculate_mark(points, max_points)


for student, grade in grade_dict.items():
    print("{} has grade: {}".format(student, grade))
