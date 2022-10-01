inventory = {"Apple": 512, "Banana": 100}

for fruit, count in inventory.items():
    print(f"There are {count} {fruit} in store")

for fruit in inventory.keys():
    print(f"We have {fruit} in the inventory")


total_count = 0
for count in inventory.values():
    total_count += count

print(f"There are {total_count} fruits in store")


grades = {"Tom": 4.5, "Philipp": 4}

sum_of_grades = 0
for grade in grades.values():
    sum_of_grades += grade

print(f"The average grade was {sum_of_grades/len(grades)}")
