def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark * 2) * 0.5


max_points = int(input('Enter maximum score\n'))

while True:
    name = input('Enter the name\n')
    if name == 'exit':
        break
    points = input('Enter points\n')
    
    print(calculate_mark(points, max_points))


