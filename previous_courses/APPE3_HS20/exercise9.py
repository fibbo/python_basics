def calculate_mark(points, max_points):
    return float(points) * 5 / float(max_points) + 1

max_points = input('Please enter maximum possible points: ')

grade_dict = {}

while True:
    name = input('Please enter the name or type exit to quit: ')
    if name.lower() == 'exit':
        # Print students names & grades
        break
    points = input('Please enter points scored: ')
    grade_dict[name] = calculate_mark(points, max_points) 

# Print students names & grades
# print({})

sum_of_grades = 0
for name, grade in grade_dict.items():
    sum_of_grades += grade
    if grade >= 4:
        print(f'{name} passed with grade {grade}')
    else:
        print(f'{name} failed with grade {grade}')

print(f'The average grade is {sum_of_grades/len(grade_dict)}')


print(f'The average grade is {sum(grade_dict.values())/len(grade_dict)}')