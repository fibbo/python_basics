def calculate_mark(points, max_points):
    return points * 5 / max_points + 1


max_points = int(input('Please enter max score: '))
grades = {}

while True:
    name = input('Please enter the name of the student or type exit to quit: ')
    if name== 'exit':
        break
    points = float(input('Please enter points scored: '))
    grades[name] = calculate_mark(points, max_points)

sum_of_grades = 0
for name, grade in grades.items():
    sum_of_grades += grade
#   sum_of_grades = sum_of_grades + grade
    if grade >= 4:
        print('{} has passed with grade {}'.format(name, grade))
    else:
        print('{} has failed with grade {}'.format(name, grade))

print('Average grade: {}'.format(sum_of_grades/len(grades)))


# Alternate solution for average:
print('Average grade: {}'.format( sum( grades.values() ) / len(grades)) )

# Explanation:
# grades.values() <- returns list of all values aka grades
# sum( list ) <- returns the sum of all elements in the list
# and then just divide the sum by the number of students == len(grades)