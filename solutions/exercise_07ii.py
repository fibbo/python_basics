def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round_to(mark, 0.5)


max_points = int(input("Enter maximum score: "))

while True:
    name = input("Enter the name: ")
    if name == "exit":
        break
    points = int(input("Enter points: "))

    print(calculate_mark(points, max_points))
