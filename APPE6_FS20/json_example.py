import json

my_dict = {'one': 'eins', 'two': 'zwei', 'three': 'drei'}
print(type(my_dict))

my_dict_as_string = json.dumps(my_dict)
print(type(my_dict_as_string))

with open('json.txt', 'w') as file:
    file.write(my_dict_as_string)


    