def compare(x, y):
  if x > y:
    print(1)
  elif x < y:
    print(-1)
  else:
    print(0)


x_input = int(input("Enter value 1\n"))
y_input = int(input("Enter value 2\n"))

compare(x_input, y_input)