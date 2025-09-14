# Dictionaries: {}

## Key-Value pair

- Dictionaries are very similar to lists but have a key and value for each entry
- The entries of a dictionary are not sorted

## Creating dictionaries

Dictionaries are created using {}

```python
eng2de = {}
eng2de["one"] = "eins"
eng2de["two"] = "zwei"
```

Values can be added directly

```python
inventory = {
"apples": 430,
"bananas": 312,
}
```

## Accessing entries

Values can be accessed directly using dictionary["key"]

```python
inventory = {
"apples": 430,
"bananas": 312,
}
print(inventory["apples"])
# 430
```

## Assigning and modifying values

- The key is assigned a value
- If the key already exists the existing value is overwritten

```python
inventory = {
"apples": 430,
"bananas": 312,
}
inventory["oranges"] = 530
inventory["bananas"] = 250
print(inventory["bananas"])
# 250
```

## Deleting entries

Key-Value pairs can be deleted using the `del()` function

```python
inventory = {
"apples": 430,
"bananas": 312,
}
del(inventory["bananas"])
```

## Number of entries

The `len()` function returns the number of entries

```python
inventory = {
  "apples": 430,
  "bananas": 312,
}
len(inventory)
# 2
```

## Checking if an entry exists

The `in` keyword can be used to check if a key exists in a dictionary

```python
inventory = {
  "apples": 430,
  "bananas": 312,
}
if "apples" in inventory:
  inventory["apples"] += 100
else:
  inventory["apples"] = 100
```

## Iterating over entries

The `items()` function combined with the `for` statement can be used to iterate through every key-value pair

```python
for (my_key, my_value) in my_dict.items():
  print(my_key + ' : ' + my_value)
```

______________________________________________________________________

**Previous:** [Functions](03_08_functions.md) | **Next:** [Persistence](04_persistence.md)
