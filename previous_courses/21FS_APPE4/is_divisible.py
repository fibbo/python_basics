def is_divisible(x, y):
  if x % y == 0:
    return True
  else:
    return False

a = 4
b = 3
if is_divisible(a, b):
  print(f'{a} is divisible by {b}')
else:
  print(f'{a} is not divisible by {b}')