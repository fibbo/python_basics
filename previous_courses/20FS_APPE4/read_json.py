import json

loaded_dictionary = {}
with open("my_dict.dat", "r") as f:
    for line in f:
        line = line.strip()
        loaded_dictionary = json.loads(line)


for (key, value) in loaded_dictionary.items():
    print(key, value)
