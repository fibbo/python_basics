# Immutables: Tuples () and Strings

## Tuples

Tuples is an immutable sequence data type

- It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.
- Tuples are declared using () instead of []

```python
tuple = ("a", "b", "c", "d", "e")
```

Tuples containing only one element (singleton) must have a comma at the end of the definition

```python
tuple = ("a", )
```

## Strings

Strings are immutable

- Unlike lists, strings cannot be changed
- Operations on strings always return a modified copy of the string
- The original string remains unchanged

```python
greeting = "Hello, world!"
greeting[0] = "J"
# TypeError: 'str' object does not support item assignment
```

______________________________________________________________________

**Previous:** [Lists](03_05_lists.md) | **Next:** [Iteration: for & while](03_07_iteration_for_while.md)
