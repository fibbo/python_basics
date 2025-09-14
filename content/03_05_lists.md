# Lists: []

- Lists are a data type
- Lists are used in most programming languages (arrays)
- Lists are a set of values

```python
list_a = [1, 2, 4]
list_b = ["Monty", "Python"]
```

## Creating lists

- The easiest way to create a list is using []

```python
numbers = [10, 12, 14, 19]
words = ["spam", "bungee", "swallow"]
```

- Data types can be mixed

```python
my_list = ["music", 2000, 3.5, True]
```

Since numbers are often stored in a list, there is a special method for doing so. With only one argument, range returns a number series starting at 0

```python
list(range(4))
# returns [0, 1, 2, 3]
```

When using two arguments it is possible to define the start and end of the range \[start, end) (end is not included in the list)

```python
list(range(1,5))
# returns [1, 2, 3, 4]
```

The step size can be defined with a third argument

```python
list(range(1, 10, 2))
# return [1, 3, 5, 7, 9]
```

An empty list can also be created

```python
empty_list = []
```

This is often done when the values to be inserted in the list are not yet known.

## Accessing elements

Accessing elements can be done with the [] operator

```python
names = ["Anna", "Tom", "Ralph", "Peter"]
print(names[1])
# prints Tom
```

**Important: Array indices start at 0!**

| 0 | 1 | 2 | 3 |
|------|-----|-------|-------|
| Anna | Tom | Ralph | Peter |

A negative index is used to access the list from the end

```python
names = ["Anna", "Tom", "Ralph", "Peter"]
print(names[-1])
# prints Peter
```

## Length

The number of elements in a list can be obtained using the `len()` function

```python
names = ["Anna", "Tom", "Ralph", "Peter"]
print(len(names))
# prints 4
```

## Out of range

If there is no item in the list at the desired index, Python will print an error message

```python
names = ["Anna", "Tom", "Ralph", "Peter"]
n_names = len(names)
print(names[n_names])
# IndexError: list index out of range
```

## Changing elements in a list

An element can be changed using [INDEX]

```python
names = ["Anna", "Tom", "Ralph", "Peter"]
names[0] = "Alice"
# ["Alice", "Tom", "Ralph", "Peter"]
```

## Adding elements

The `append()` method can be used to add an element at the end of the list

```python
numbers = list(range(5))
# [0, 1, 2, 3, 4]
numbers.append(5)
# [0, 1, 2, 3, 4, 5]
```

## Concatenate lists

The + operator can be used to join lists

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# [1, 2, 3, 4, 5, 6]
```

## Slices

Lists can be cut into slices. The operator [n:m] returns a list of the elements that start at index n and stop before m

```python
my_list = ["a", "b", "c", "d", "e", "f"]
my_list[1:3]
# ["b", "c"]
```

If the first index is empty, the slice starts at the beginning

```python
my_list = ["a", "b", "c", "d", "e", "f"]
my_list[:4]
# ["a", "b", "c", "d"]
```

If the second index is empty, the slice will include elements until the end of the list

```python
my_list = ["a", "b", "c", "d", "e", "f"]
my_list[3:]
# ["d", "e", "f"]
```

## Deleting elements

The `del()` method deletes items from the list

```python
list_a = ["one", "two", "three"]
del(list_a[1])
# ["one", "three"]
list_b = ["a", "b", "c", "d", "e", "f"]
del(list_b[1:5])
# ["a", "f"]
```

______________________________________________________________________

**Previous:** [Conditionals: if, else, elif](03_04_conditionals_if_else_elif.md) | **Next:** [Immutables: Tuples & Strings](03_06_immutables_tuples_strings.md)
