def proper_round(number):
    decimal_part = number - int(number)
    if decimal_part >= 0.75:
        decimal_part = 1.0
    elif decimal_part >= 0.25:
        decimal_part = 0.5
    else:
        decimal_part = 0.0
    return int(number) + decimal_part


def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return proper_round(mark)


max_points = int(input("Enter maximum score: "))

student_grades = {}

while True:
    name = input("Enter the name: ")
    if name == "exit":
        break
    points = input("Enter points: ")

    print(calculate_mark(points, max_points))
    student_grades[name] = calculate_mark(points, max_points)

sum_of_grades = 0
counter = 0
for name, grade in student_grades.items():
    sum_of_grades += grade
    counter += 1
    if grade >= 4:
        print("{} has passed with grade {}".format(name, grade))
    else:
        print("{} has failed with grade {}".format(name, grade))

print("The class average is {}".format(sum_of_grades / counter))
print("The class average is {}".format(sum_of_grades / len(student_grades)))


print(
    "The class average is {}".format(sum(student_grades.items()) / len(student_grades))
)
