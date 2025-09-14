# Conditionals: if/else/elif

- Boolean algebra is a part of mathematics
- Often used in programming
- A boolean expression is either true or false

```python
print(5 == 5) # --> True
print(5 == 6) # --> False
print(6 > 4) # --> True
print(5 >= 8) # --> False
```

## `if`

- The expression if defines a condition
- If the condition is true, subsequent statements will be executed
- If the condition is false, subsequent statements will not be executed
- There has to be at least one statement after the condition

```python
x = 10
if x > 0:
  print(f"{x} is positive")
if True:
  # This statement will always be executed
  print("Yes")
if False:
  # This statement will never be executed
  print("No")
```

## `else`

- Expression else is executed if the if condition is false
- Can only be used in combination with an if expression

```python
if x == 0:
  print("x is zero")
else:
  print("x is not zero")
```

**%-operator (remainder after division)**

```python
if x % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
```

## Chained conditionals

- `elif` is used to combine multiple conditions
- The `else` expression is executed when neither `if` nor any of the `elif`s is true.
- Any number of `elif` expressions can be used but only one `if` and one `else`

```python
if x < y:
  print(f"{x} is less than {y}")
elif x > y:
  print(f"{x} is greater than {y}")
else:
  print(f"{x} and {y} are equal")
```

```python
# Python 3
answer = input("Do you like Python?")
if answer == "yes":
  print("That is great!")
else:
  print("That is disappointing!")
```

## Nested conditionals

Conditionals can be nested

```python
if x > 0:
  if x < 10:
    print("x is a positive single digit")
```

## and

- Deep nesting can be difficult to read
- Use `and` to combine conditionals

```python
if x > 0:
  if x < 10:
    print("x is a positive single digit")
# is the same as
if x > 0 and x < 10:
  print("x is a positive single digit")
```

## or

- At least one statement must be true for the condition to be true

```python
if x > 0 or x < 0:
  print("x is not zero")
```

## not

- Negation, inverts the boolean.
- `not` True -> becomes False
- `not` False -> becomes True

```python
is_weekend = False
if not is_weekend:
  print("Time to go to work!")
else:
  print("Enjoy your weekend!")

# This is equivalent to:
if is_weekend == False:
  print("Time to go to work!")
else:
  print("Enjoy your weekend!")
```

**Truth Table**

| X | Y | X and Y | X or Y |
|-------|-------|---------|--------|
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

______________________________________________________________________

**Previous:** [Naming Conventions & Debugging](03_03_naming_conventions_debugging.md) | **Next:** [Lists](03_05_lists.md)
