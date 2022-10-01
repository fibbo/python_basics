number_list = [1, 2, 3, 4, 5, 3, 10, 14, 12, 19, 17, 7, 6, 5]

index = number_list.index(5)
print(number_list[index])

try:
    print(number_list.index(99))
except ValueError:
    print("Element not found")


indices = [i for i, j in enumerate(number_list) if j == 5]


for i, j in enumerate(number_list):
    print(i, j)
