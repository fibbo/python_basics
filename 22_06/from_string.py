import json

my_dict_as_string = '{"two": "zwei", "one": "eins"}'

my_dict = json.loads(my_dict_as_string)

print(my_dict)
print(type(my_dict_as_string))
print(type(my_dict))
