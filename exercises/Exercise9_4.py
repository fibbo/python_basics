def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round(mark * 2) / 2


max_points = int(input('Enter maximum score\n'))

grade_dict = {}

while True:
    name = input('Enter the name\n')
    if name == 'exit':
        break
    points = input('Enter points\n')
    grade_dict[name] = calculate_mark(points, max_points)

avg = 0

for (name, grade) in grade_dict.items():
    avg += grade
    if grade >= 4:
        print('{} has passed with {}'.format(name, grade))
    else:
        print('{} has failed with {}'.format(name, grade))

avg /= len(grade_dict)
print('Average: ' + str(avg))

print('Average: ' + str(sum(list(grade_dict.values()))/len(grade_dict)))
