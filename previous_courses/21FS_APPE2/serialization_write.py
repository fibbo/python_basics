import json

my_dict = {'one': 'eins', 'two': 'zwei'}

my_dict_as_string = json.dumps(my_dict)

with open('data.txt', 'w') as f:
    f.write(my_dict_as_string)