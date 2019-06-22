def calc_sum(numbers):
    index = 0
    # sum variable to keep track of the result
    sum = 0
    while index < len(numbers):
        # keep track of the sum
        sum = sum + numbers[index]
        # increase index by one
        index = index + 1
    return sum


print(calc_sum(list(range(1001))))
print(calc_sum([4, 6, 7]))
