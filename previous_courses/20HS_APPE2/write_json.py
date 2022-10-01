import json


eng2de = {"one": "eins", "two": "zwei"}

print(eng2de)

eng2de_string = json.dumps(eng2de)


with open("dict_json.txt", "w") as f:
    f.write(eng2de_string)
