def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1
    return mark


max_points = input("Enter the maximum points possible: ")
grades = {}

while True:
    name = input("Please enter the student's name or type 'exit' to quit: ")
    if name.lower() == "exit":
        # print all the grades here
        break
    points = input("Please enter the points scored: ")

    grades[name] = calculate_mark(points, max_points)

summe = 0
for name, grade in grades.items():
    if grade >= 4:
        print(f"{name} has passed with grade {grade}")
    else:
        print(f"{name} has failed with grade {grade}")
    summe += grade

average = summe / len(grades)
print(f"Average grade is {average}")

average_2 = sum(grades.values()) / len(grades)
print(f"Average grade is {average_2}")
