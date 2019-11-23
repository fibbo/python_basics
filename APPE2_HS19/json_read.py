import json

dictionary = {}

with open('dictionary.txt', 'r') as file:
    for line in file:
        dictionary = json.loads(line.strip())


print(dictionary['one'])
print(type(dictionary))