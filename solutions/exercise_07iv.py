def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round_to(mark, 0.5)


def main():
    max_points = int(input("Enter maximum score: "))
    grade_dict = {}

    while True:
        name = input("Enter the name or type exit to quit: ")
        if name == "exit":
            break
        points = input("Enter points: ")
        grade_dict[name] = calculate_mark(points, max_points)

    avg = 0

    for name, grade in grade_dict.items():
        avg += grade
        if grade >= 4:
            print("{} has passed with {}".format(name, grade))
        else:
            print("{} has failed with {}".format(name, grade))

    avg /= len(grade_dict)
    print(f"Average: {avg}")

    print(f"Average: {str(sum(list(grade_dict.values())) / len(grade_dict))}".format())


main()
