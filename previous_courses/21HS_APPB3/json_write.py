import json

my_dict = {"one": "eins", "two": "zwei"}
my_dict_as_string = json.dumps(my_dict)
print(my_dict_as_string)

with open("python_dict.dat", "w") as f:
    f.write(my_dict_as_string)
