import json

my_dict = {"one": "eins", "two": "zwei"}
my_dict_as_string = json.dumps(my_dict)

print(my_dict_as_string)
print(type(my_dict_as_string))

print(my_dict)
print(type(my_dict))

with open("dict.json", "w") as f:
    f.write(my_dict_as_string)
