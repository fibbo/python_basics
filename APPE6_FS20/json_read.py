import json

new_dict = {}
with open('json.txt', 'r') as file:
    for line in file:
        line = line.strip()
        new_dict = json.loads(line)

print(type(new_dict))
for key, value in new_dict.items():
    print('{} {}'.format(key, value))
