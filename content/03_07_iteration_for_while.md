# Iteration: for/while

- Iterations are used to repeat statements
- There are two expressions for iterations
  - `while`
  - `for`

## while

As long as the condition of the while loop is True, the body of the loop gets executed

```python
while n > 0:
  print(n)
  n = n - 1
print('Lift off!')
```

- If the condition is False at the beginning, the body of the loop is never executed
- If the variable that is used to check the condition of the while loop does not change, the loop will never terminate -> infinite loop
- Whether a while loop terminates can be hard to determine

```python
while n != 1:
  print(n)
  if n % 2 == 0:
    n = n / 2
  else:
    n = n * 3 + 1
```

A `while` loop can be used to iterate through a list

```python
names = ["Tom", "Anna", "Christopher"]
index = 0
while index < len(names):
  name = names[index]
  print(name)
  index = index + 1
```

## for

Since it is often necessary to operate through lists and other data types, there is a special expression for this

```python
for element in element_list:
  print(element)
```

______________________________________________________________________

**Previous:** [Immutables: Tuples & Strings](03_06_immutables_tuples_strings.md) | **Next:** [Functions](03_08_functions.md)
