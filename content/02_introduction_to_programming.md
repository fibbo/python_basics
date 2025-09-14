# Introduction to Programming

## What is a Computer Program

**Modular System**

- **Input**: Data input from keyboard, files, internet, etc...
- **Output**: Processed data is displayed or saved to a file
- **Algorithms**: The computer's cooking recipes
- **Libraries**: Using existing implementations (can do anything of the above)

## Why Python?

- High-level programming language
- "Simple" syntax
- Cross-platform - A script written on a Windows computer also runs on Linux & Mac
- Interpreted => Easy to run
- Many libraries available

## Examples: Hello World

High level languages but not trivial to learn:

**Java**

```java
public class HelloWorld {
  public static void main(String args[]) {
    System.out.println("Hello World");
  }
}
```

**C++**

```cpp
#include <iostream>
int main() {
  std::cout << "Hello World\n";
  return 0;
}
```

Or even worse:

**Machine Language**

```
.LC0:
  .string "Hello world!"
main:
  push rbp
  mov rbp, rsp
  mov edi, OFFSET FLAT:.LC0
  mov eax, 0
  call printf
  mov eax, 0
  pop rbp
  ret
```

**Python**

```python
print("Hello World")
```

## How to Run Python Code

**Options to run Python code:**

- Directly in the Python prompt (REPL - Read, Eval, Print, Loop)
- Write the code into a file and run python with the file
- Use IDE to run Python code

## Development Environment

- Integrated Development Environment (IDE)
- Collection of tools that are commonly used for software development (they make our life easier!)
- Popular IDEs
  - Visual Studio Code - https://code.visualstudio.com
  - JetBrains PyCharm - Community Edition available for free http://jetbrains.com/pycharm/download
- It takes time to get proficient using an IDE

______________________________________________________________________

**Previous:** [General Introduction](01_general_introduction.md) | **Next:** [Variables, Types, Expressions, Operators, Comments](03_01_variables_types_expressions_operators_comments.md)
