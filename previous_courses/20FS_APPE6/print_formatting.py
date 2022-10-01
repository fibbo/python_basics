a = 20
b = 10
c = a + b

# print('The sum of ' + str(a) + ' and ' + str(b) + ' is ' + str(c))

# {} are placeholders which python will the replace
# with the arguments provided in the .format() part
print("The sum of {1} and {0} is {2}".format(a, b, c))

print("The sum of %s and %s is %s" % (a, b, c))
