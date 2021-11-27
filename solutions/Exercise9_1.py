import math

def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int(n / precision + correction) * precision


def calculate_mark(points, max_points):
    mark = float(points) * 5.0 / float(max_points) + 1
    return round_to(mark)

print(calculate_mark(18, 40))
