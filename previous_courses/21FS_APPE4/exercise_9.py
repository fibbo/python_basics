def calculate_mark(points, max_points):
  mark = points * 5 / max_points + 1
  return mark

max_points = input('Please enter the maximum possible score: ')

# 9.2
grades_dictionary = {}

while True:
  # 9.2 Also read name from input
  name = input('Please enter the name of the student or type exit to quit: ')
  if name.lower() == 'exit':
    break
  points = input('Please enter the student: ')

  # 9.2 Store name/grade key-value pair in the dictionary
  grades_dictionary[name] = calculate_mark(float(points), float(max_points))


# 9.3 Print all the names & grades of the students
# 9.4 Also print whether a student passed or failed
sum_of_grades = 0
for name, grade in grades_dictionary.items():
  sum_of_grades += grade # equal to: sum_of_grades = sum_of_grades + grade
  if grade >= 4.0:
    print(f'{name} passed with grade {grade}')
  else:
    print(f'{name} failed with grade {grade}')


# 9.5 Calculate class average grade
print(f'The class average is {sum_of_grades/len(grades_dictionary)}')

# Another way to calculate the average
average = sum(grades_dictionary.values()) / len(grades_dictionary)
print(f'The class average is {average}')
