def calculate_mark(points, max_points):
    return float(points) * 5 / float(max_points) + 1


max_points = input("Please enter maximum possible points: ")

grades_dict = {}

while True:
    name = input("Please enter students name or type exit to quit: ")
    if name == "exit":
        break
    points = input("Please enter points scored: ")
    grades_dict[name] = calculate_mark(points, max_points)
    # grades_dict = { name: calculate_mark(points, max_points)}


sum_of_grades = 0
for name, grade in grades_dict.items():  # .keys() .values()
    sum_of_grades += grade
    if grade >= 4:
        print(f"{name} has passed with grade {grade}")
    else:
        print(f"{name} has failed with grade {grade}")

print(f"The average grade is {sum_of_grades / len(grades_dict)}")

# Other way to calculate average - doesn't need a for loop
average = sum(grades_dict.values()) / len(grades_dict)
print(average)
