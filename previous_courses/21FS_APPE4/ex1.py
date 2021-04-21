def compare(x, y):
  if x > y:
    print(1)
  elif x < y:
    print(-1)
  else:
    print(0)

value_1 = int(input("Please enter first number: "))
value_2 = int(input("Please enter second number: "))

compare(value_1, value_2)