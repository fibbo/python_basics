# Functions

## Built-in Functions

Function are self contained modules of code that accomplish a specific task. They usually "accept" input data and "return" a result.

```python
name = "Some name"
print(name) # Some name is used inside the print function -> the print function accepts the input and prints it to the console
```

Functions can (and often do) also return a result (but the print function does not)

```python
text = "Python programming language"
print(text) # Prints: Python programming language
text_length = len(text) # This function returns the length of the text
print(text_length) # Prints length of the string
```

**Built-In Functions:** https://docs.python.org/3/library/functions.html

## Functions, First Library

**Library import**

```python
import math
log_res = math.log(17.0)
sin_res = math.sin(45) # WRONG (well, not really, but not what we want)

sin_res = math.sin(math.radians(45))  # cos/sin etc take radians as arguments -> conversion from degree to radians necessary
```

More info: http://docs.python.org/library/math.html

## User-Defined Functions

**User-defined functions**

- A function encapsulates some functionality
- Reduces complexity

```python
def print_two_values(param1, param2):
  print(param1)
  print(param2)
```

- Syntax is important
  - Indentation
  - The colon

```python
def line_separator():
  print("")

print("First Line")
line_separator()
print("Second Line")
line_separator()
print("Third Line")
line_separator()
print("Fourth Line")
```

If we want to change the line separator to a dashed line we only need to change a single line of code

```python
def line_separator():
  print("------------------------------")
```

If the line separator should output two lines we can define a new function that calls the `line_separator()` function twice

```python
def two_lines():
  line_separator()
  line_separator()

print ("First Line")
two_lines()
print("Second Line")
```

**Parameters and arguments**

- Arguments are passed when calling a function
- Value of arguments is assigned to parameters

```python
def print_sum(number_1, number_2):
  result = number_1 + number_2
  print(result)

print_sum(1, 3)
print_sum(10, 5)
```

- Parameters are variables valid within the scope of the function
- Variables that are defined in a function can only be seen inside that function
- Scope can be identified by indentation

```python
def concatenation(param1, param2):
  concat = param1 + param2
  print(concat)

concatenation("Hello", "World")
print(concat) # NameError: name 'concat' is not defined
```

**Conclusion**

- A function can be called multiple times
- If some code can be reused, put it in a function so you need to write less code
  - Higher factorization
  - Less redundancy
  - Better maintenance
- Functions can also call other functions

## Functions with return value

Some functions will return a value

```python
# Python 3
answer = input("Do you like Python?")
```

Our previously defined functions have never returned anything, but only printed something out

### return

Functions that return a value use the `return` keyword

```python
import math
def area(radius):
  result = math.pi * radius ** 2
  return result

print(area(10))
my_circle_area = area(8)
```

Functions can return any valid data type

### Boolean return values

- The functions can return a boolean value (True, False)
- The function name should be formulated as a yes/no question

```python
def is_divisible(x, y):
  return x % y == 0
```

The return value can be used in a condition

```python
if is_divisible(x, y):
    print(f"{x} is divisible by {y}")
else:
    print(f"{x} is not divisible by {y}")
```

______________________________________________________________________

**Previous:** [Iteration: for & while](03_07_iteration_for_while.md) | **Next:** [Dictionaries](03_09_dictionaries.md)
