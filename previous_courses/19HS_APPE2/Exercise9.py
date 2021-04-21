def custom_round(value):
    decimal_part = value - int(value)
    if decimal_part < 0.25:
        return int(value)
    if decimal_part < 0.75:
        return int(value) + 0.5
    return int(value) + 1

def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1
    return custom_round(mark)


some_string = "Some text"

max_points = input("Please enter the maximum score of the test: ")


grade_dict = {}
while True:
    name = input("Please enter the student's name or type exit to: ")
    if name == 'exit':
        break
    points = input("Please enter the student's score: ")

    grade_dict[name] = calculate_mark(points, max_points)

sum_of_grades = 0
for name, grade in grade_dict.items():
    sum_of_grades += grade
    if grade >= 4:
        print('{} has passed with grade {}'.format(name, grade))
    else:
        print('{} has failed with grade {}'.format(name, grade))

print('The average is {}'.format(sum_of_grades / len(grade_dict)))


average = sum(list(grade_dict.values())) / len(grade_dict)
print(average)
