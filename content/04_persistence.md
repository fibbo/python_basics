# Persistence

So far no data has been saved in any of our examples. All data was deleted from the memory as soon as our examples quit. There are several ways to permanently store data on the hard disk:

- Database
- Simple text files

## Files

### Common procedure

- Open file
- Do something with the file
- Close the file - depending on syntax done automatically.

```python
with open('my_file.txt', "mode") as file:
  # do some stuff
```

### Different modes

The mode defines how the content of the file should be treated

**Modes**

- "r": read only
- "w": write only
- "r+": read and write
- "a": append

```python
# open a file in read/write mode
with open('my_file.txt', "r") as file:
  # do some stuff
```

### Write

- The write() function is used to write something into a file
- `'\n'` is used to insert a line break

```python
with open('my_file.txt', "a") as file:
  file.write('First line of the write operation')
  file.write('This is a line with a new-line character at the end\n')
  file.write('This is another line, on a new-line below the previous one.\n')
```

### Read

- A `for` loop can be used to read a file line by line
- `line.strip()` removes the trailing `'\n'`

```python
with open('my_file.txt', "r") as file:
  for line in file:
    line = line.strip()
    print(line)
```

## JSON

### Dictionaries/list in JSON

- file.write() only accepts strings as arguments
- If complex structures such as dictionaries or lists should be stored in a file, it's necessary the convert these structures into strings first
- An example of a standard used for this purpose is JSON (Javascript Object Notation)

```python
import json
my_dict = {"one": "eins", "two": "zwei"}
my_dict_as_string = json.dumps(my_dict)
print(my_dict_as_string)
```

### Convert JSON to dictionaries/lists

Example of a string in JSON that is converted into a dictionary

```python
import json
my_dict_as_string = '{"two": "zwei", "one": "eins"}'
my_dict = json.loads(my_dict_as_string)
print(my_dict)
```

______________________________________________________________________

**Previous:** [Dictionaries](03_09_dictionaries.md) | **Next:** [Additional Resources](05_additional_resources.md)
