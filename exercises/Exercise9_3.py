def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round(mark * 2) * 0.5


max_points = input('Enter maximum score\n')

grade_dict = {}

while True:
    name = input('Enter the name\n')
    if name == 'exit':
        break
    points = input('Enter points\n')
    grade_dict[name] = calculate_mark(points, max_points)


for (name, grade) in grade_dict.items():
    if grade >= 4:
        print(name + ' has passed with ' + str(grade))
    else:
        print(name + ' has failed with ' + str(grade))
