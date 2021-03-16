def calculate_mark(points, max_points = 100):
  return float(points) * 5 / float(max_points) + 1


def calculate_all_grades():
  max_points = input('Please enter maximum possible points: ')

  while True:
    points = input('Please enter points scored or type exit to quit: ')
    if points == 'exit':
      break
    print(calculate_mark(points, max_points))


def print_addresses():
  print('Print addresses here')


while True:
  command = input('Type print to print addresses or grading to grade a test: ')
  if command == 'print':
    print_addresses()
  elif command == 'grading':
    calculate_all_grades()
  elif command == 'exit':
    break