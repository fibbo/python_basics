def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1
    return mark


max_points = input("Please enter maximum possible points: ")

grade_dictionary = {}

while True:
    name = input('Please enter the student\'s name or type exit to quit: ')
    if name == 'exit':
        break
    points = input('Please enter points scored: ')

    grade_dictionary[name] = calculate_mark(points, max_points)
    # mark = calculate_mark(points, max_points)
    # print(mark)

sum_of_grades = 0
for (name, grade) in grade_dictionary.items():
    if grade >= 4.0:
        print('{} has passed with grade: {}'.format(name, grade))
    else:
        print('{} has failed with grade: {}'.format(name, grade))
    
    sum_of_grades += grade # += -> sum_of_grades = sum_of_grades + grade

print('The class average is {}'.format(sum_of_grades / len(grade_dictionary)))


print('The class average is {}'.format(sum(grade_dictionary.values()) / len(grade_dictionary)))