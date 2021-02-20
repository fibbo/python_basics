import json

new_dict = {}
with open('data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        new_dict = json.loads(line)


print(new_dict['one'])
