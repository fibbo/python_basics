import json

my_dict = {"one": "eins", "two": "zwei"}
my_dict_as_string = json.dumps(my_dict)
print(my_dict)
print(my_dict_as_string)

with open("dictionary.txt", "w") as file:
    file.write(my_dict_as_string)
