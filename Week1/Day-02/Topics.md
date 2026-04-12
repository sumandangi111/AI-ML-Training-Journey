# Day 02 - Variables, Literals & Input/Output 

---

## 📌 Variables in Python

A variable is used to store data in memory.

### Example:
```python
x = 10
name = "Suman"

👉 Python is dynamically typed (no need to declare data type)

📌 Variable Naming Rules
Must start with a letter (a-z, A-Z) or underscore (_)
Cannot start with a number
Cannot use keywords (if, else, for, etc.)
Case-sensitive (name and Name are different)
Valid Examples:
name = "Suman"
_age = 20
total_marks = 95
Invalid Examples:
1name = "Suman"   # ❌
class = 10        # ❌ (keyword)
📌 Literals in Python

Literals are fixed values assigned to variables.

Types:
Numeric → 10, 3.14
String → "Hello"
Boolean → True, False
Example:
x = 10
name = "Python"
flag = True
📌 Constants in Python

Constants are values that should not change during program execution.

👉 Python does not have strict constants, but we use uppercase naming convention.

Example:
PI = 3.14
MAX_VALUE = 100
📌 Input Function

Used to take input from the user.

Example:
name = input("Enter your name: ")
print("Hello", name)

👉 By default, input() returns a string

📌 Type Casting

Used to convert data types.

Example:
age = int(input("Enter your age: "))
print(age + 5)
📌 Output Function

Used to display output.

Example:
print("Hello World")