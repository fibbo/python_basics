def proper_round(number):
    decimal_part = number - int(number)
    if decimal_part >= 0.75:
        decimal_part = 1.0
    elif decimal_part >= 0.25:
        decimal_part = 0.5
    else:
        decimal_part = 0.0
    return int(number) + decimal_part

def calculate_mark(points, max_points):
    # convert strings to numbers
    mark = float(points) * 5 / float(max_points) + 1
    return proper_round(mark)


max_points = input('Please enter maximum possible points: ')

# for 9iii: Dictionary for the grades. 
# Keys are names, values are the grades
grades = {}

while True:
    # For 9iii: Also ask for name, do the exit check on the name
    # instead on the points. It makes the program flow better
    name = input('Please enter the name or type exit to quit: ')
    if name == 'exit':
        break
    points = input('Please enter points scored: ')
    
    print(calculate_mark(points, max_points))

    # For 9iii: Store the grade with the corresponding name
    # in the dictionary. NB: If 2 students have the same name,
    # we will have a problem
    grades[name] = calculate_mark(points, max_points)


# for 9iii: Print all the names and grades
sum_of_grades = 0
for student, grade in grades.items():
    sum_of_grades += grade
    # For 9iv:
    if grade >= 4:
        print('{} has passed with grade {}'.format(student, grade))
    else:
        print('{} has failed with grade {}'.format(student, grade))

print('The average grade is {}'.format(sum_of_grades/len(grades)))

average_grade = sum(grades.values())/len(grades)
print('The average grade is {}'.format(average_grade))