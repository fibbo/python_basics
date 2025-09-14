# Variables, Types, Expressions, Operators, Comments

## Variables

Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program.

- Variables hold values
- Similar to mathematics
  - x = 2
  - y = x + 2
- Values assigned using the `=` operator

## Data Types

**Types**

- Numbers (Integers, Floats)
  - 2
  - 1000000
  - -2
  - 3.2
  - 1.333333

**Strings**

- Strings (Text)
  - 'Hello World'
  - "Hello World"
- 'Single quotes' or "double quotes" can be used to create them
  - 'Hello World'
  - "Hello World"
  - "5"

**Boolean**
Binary data type

- True
- False

**None Type**

- `None` represents "nothing" or "no value"
- Think of it like an empty box - the box exists, but there's nothing inside
- Common examples:
  - A person's middle name when they don't have one
  - The result when a function doesn't return anything
  - An uninitialized variable

```python
middle_name = None  # Person has no middle name
print(middle_name)  # Prints: None

# Functions that don't return anything give None
result = print("Hello")  # print() returns None
print(result)  # Prints: None
```

## Variables

Use meaningful names

**Declaration**

```python
salutation = "Hello"
name = "Monty Python"
pi = 3.14159
```

**Usage**

```python
print(name)
```

**Variables and values can be combined**

```python
a = 3
b = 8.3
c = a + b
print(c)

salutation = "Hello"
name = "Monty Python"
print(salutation + " " + name) # String concatenation with +
```

**Keywords - reserved words**

You cannot name a variable with these names as they are protected by the language.

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

## Operators

**Order of precedence (kind of like PEMDAS)**

- ()
- \*\*
- unary + -
- - / % //
- binary + -
- `<`, `>`, `<=`, `>=`, `!=`, `==`
- **not**
- **and**
- **or**

## Comments

- Comments have no impact on the program
- Should explain the code
- A comment starts with a # character

```python
# Declaring the name
name = "Philipp"
print(name) # Prints Philipp
```

______________________________________________________________________

**Previous:** [Introduction to Programming](02_introduction_to_programming.md) | **Next:** [Input and Output](03_02_input_and_output.md)
