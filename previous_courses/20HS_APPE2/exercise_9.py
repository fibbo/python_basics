def calculate_marks(points, max_points):
    return float(points) * 5 / float(max_points) + 1



max_points = input('Please enter the maximum possible points: ')
grade_dict = {}
while True:
    name = input('Enter the students name or type exit to quit: ')
    if name == 'exit':
        break
    points = input('Please enter points scored: ')
    print(calculate_marks(points, max_points))
    grade_dict[name] = calculate_marks(points, max_points)

# The printing stuff down here
print(grade_dict)

sum_of_grades = 0
for (name, grade) in grade_dict.items():
    sum_of_grades += grade
    if grade >= 4.0:
        print(f'{name} passed with grade {grade}')
    else:
        print(f'{name} failed with grade {grade}')

average_grade = sum_of_grades / len(grade_dict)
print(f'The average grade is: {average_grade}')

sog = sum(grade_dict.values())

print(f'The average grade is: {sog/len(grade_dict)}')

# some_variable = 1
# print(f'some string {some_variable}')

# print('some string {}'.format(some_variable))