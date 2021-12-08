import json

eng2de = {}

with open("python_dict.dat", "r") as f:
    for line in f:
        line.strip()
        eng2de = json.loads(line)

for eng, de in eng2de.items():
    print(f"{eng} is {de} in german")
