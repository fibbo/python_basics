# Input and Output

## How to Print to Console in Python

Printing is useful to provide feedback to the user or sometimes to debug your program. Printing different data types in the same print statement can be cumbersome.

- `print()` is the function to print something to console in python

```python
print("This prints just a string")
answer = 42
print(answer)  # Just print a number
print("Combining a string and a number: " + str(answer)) # Need to convert to string
print(f"Much cleaner way to print string and a number: {answer}")
```

## Input and Type Conversions

Assume you want to program a calculator. In order to do this the user needs to be able to input his numbers and the program should be able to read this. Here comes the `input` function into play.

```python
print("Add two numbers")
a = input("Please enter the first number ")
b = input("Please enter the second number ")

print("The result of the two numbers is: ")
print(a + b) # Something is wrong here
```

Sometimes it is necessary to convert a variable from one data type to another (if possible). If you read data from a file into python, at first all the data is interpreted as strings even if your file only contains numbers.

In order to do mathematical analysis on these numbers, they need to be converted to the appropriate number type first.

- `int("32")`: Converts a string that holds a number to an integer
- `int("Hello")`: This doesn't work and it will throw a ValueError exception
- `float("313.333")`: Converts a string that holds a number to a float
- `str(32)`: Converts a number to a string

Thanks to the f-string there is at least one less need to use explicit conversion functions:

```python
a = 20
b = 10
res = a + b
print(f"The sum of {a} and {b} is {res}")
# used to look like this:
print("The sum of " + str(a) + " and " + str(b) + " is " + str(res))
```

______________________________________________________________________

**Previous:** [Variables, Types, Expressions, Operators, Comments](03_01_variables_types_expressions_operators_comments.md) | **Next:** [Naming Conventions & Debugging](03_03_naming_conventions_debugging.md)
