# Naming Conventions & Debugging

## Naming Conventions

**How to name your functions and variables (PEP8)**

- Naming convention is a set of rules for choosing names of functions and variables
- Every programming language has different naming conventions
- Python
  - No spaces in variable and function names
  - Variable and function names are in lowercase and _ is used to separate words

```python
length_in_cm = 15

def say_hello():
  print("Hello")
```

## Debugging

**Finding and resolving "bugs"**

- Programming is a complex activity
- Mistakes happen all the time
- A mistake made in programming is called a bug
- The process of finding and resolving bugs is called debugging

**Errors**

- Syntax error
  - Incorrect syntax of a statement: `print(Hello World)` instead of `print("Hello World")`
- Runtime error
  - Error that occurs during the execution of a program
  - e.g. division by 0
- Semantic errors
  - Program does not deliver correct results
  - No error messages (code is syntactically correct)
  - Fixing semantic errors can be extremely complicated (good software design is important)

**Techniques**

- Reading code
- Print variables with `print()` to examine values (a poor man's debugger)
- Go through the program step by step -> **Debugger**!

______________________________________________________________________

**Previous:** [Input and Output](03_02_input_and_output.md) | **Next:** [Conditionals: if, else, elif](03_04_conditionals_if_else_elif.md)
