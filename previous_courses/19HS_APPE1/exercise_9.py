def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1

    # rounded_mark = round(2 * mark) / 2
    decimal = mark - int(mark)
    if decimal >= 0.25:
        mark = int(mark) + 0.5
    else:
        mark = int(mark)

    return mark


max_points = input("Please enter maximum score of the test: ")

grades_dict = {}

while True:
    name = input("Please enter the student's name or type exit to quit: ")
    if name == "exit":
        break

    points = input("Please enter the score of the student: ")
    grades_dict[name] = calculate_mark(points, max_points)
    # print(calculate_mark(points, max_points))


for name, grade in grades_dict.items():
    if grade >= 4:
        print("{} has passed with grade {}".format(name, grade))
    else:
        print("{} has failed with grade {}".format(name, grade))

print(sum(grades_dict.values()) / len(grades_dict))
