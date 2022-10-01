import json

dictionary = {}

print("dictionary before reading file: {}".format(dictionary))

with open("dict.json", "r") as f:
    for line in f:
        line = line.strip()
        dictionary = json.loads(line)

print("dictionary after reading file: {}".format(dictionary))

for key, value in dictionary.items():
    print(key, value)
