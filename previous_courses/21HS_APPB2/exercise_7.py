def calculate_mark(points, max_points):
    return float(points) * 5 / float(max_points) + 1


# next steps
max_points = input("Please enter maximum points possible: ")

grades = {}

while True:
    name = input("Enter the student's name or type exit to quit:")
    if name.lower() == "exit":
        break
    points = input("Enter the student's score: ")
    grades[name] = calculate_mark(points, max_points)

sum_of_grades = 0
for name, grade in grades.items():
    sum_of_grades += grade
    if grade >= 4:
        print(f"{name} has passed with with grade {grade}")
    else:
        print(f"{name} has failed with grade {grade}")


print(f"The average grade is: {sum_of_grades/len(grades)}")

print(f"The average grade is: {sum(grades.values()) / len(grades)}")
