import json

eng2de = {}


with open("dict_json.txt", "r") as f:
    for line in f:
        line = line.strip()
        eng2de = json.loads(line)


print(eng2de["one"])
