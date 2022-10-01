def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1
    return mark


max_points = input("Please enter the maximum score possible: ")

student_grades = {}

while True:
    name = input("Please enter the student's name or type exit to quit: ")
    if name == "exit":
        break

    points = input("Please enter the points scored: ")

    calculated_mark = calculate_mark(points, max_points)
    student_grades[name] = calculated_mark

    print(calculated_mark)

sum_of_grades = 0
for name, grade in student_grades.items():
    sum_of_grades += grade
    if grade >= 4:
        print("{} has passed with grade {}".format(name, grade))
    else:
        print("{} has failed with grade {}".format(name, grade))

average = sum_of_grades / len(student_grades)

print("Variant 1: The average grade was {}".format(average))

average2 = sum(student_grades.values()) / len(student_grades)

print("Variant 2: The average grade was {}".format(average2))

print("After the user entered exit, this message will show up.")
