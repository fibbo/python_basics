from datetime import date

def get_today():
  return date.today()

def print_time(time = get_today()):
  print(time)

print_time('test')
print_time()
print_time(date.ctime(date.today()))