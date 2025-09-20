def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round_to(mark, 0.5)


class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def __str__(self):
        return "id: {} \t name: {}".format(self.id, self.name)


def main():
    student_id = 0
    max_points = input("Enter maximum score: ")

    grade_dict = {}

    while True:
        name = input("Enter the name: ")
        if name == "exit":
            break
        student = Student(student_id, name)
        student_id += 1
        points = input("Enter points: ")
        grade_dict[student] = calculate_mark(points, max_points)

    for student, grade in grade_dict.items():
        print("{} has grade: {}".format(student, grade))


main()
