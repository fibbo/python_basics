a = 10
b = 20
c = a + b

# Inside a string, the curly braces serve as placeholders which are
# filled by the .format() at the end
print('a is {} and b is {} and the sum of a and b is {}'.format(a, b, c))


print('{{}} and {} and {{ }}'.format(3))