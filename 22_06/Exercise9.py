def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1
    mark = round(mark * 2) / 2
    return mark

# Read the maximum test score from keyboard input
max_score = int(input("Please enter the maximum score of the test: "))

grades_dict = {}

# Start a while loop, only exists when user enters 'exit'
while True:
    name = input("Please enter the student's name or type 'exit' to quit: ")
    if name == 'exit':
        break
    points = input("Please enter points scored: ")

    grades_dict[name] = calculate_mark(points, max_score)

sum_of_grades = 0

for name, grade in grades_dict.items():
    sum_of_grades += grade  # sum_of_grades = sum_of_grades + grade
    if grade >= 4:
        print(name + ' has passed with grade ' + str(grade))
    else:
        print(name + ' has failed with grade ' + str(grade))

print('The average grade is ' + str(sum_of_grades/len(grades_dict)))
