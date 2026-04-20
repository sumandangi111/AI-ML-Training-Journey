## Questions
1.
What is the difference between interpreted and compiled languages? Where does Python stand?

2.
Explain the difference between:
Mutable vs Immutable data types
 Give examples and explain memory behavior.

3.
What is the difference between:
=
==
is



4.
Explain all basic Python data types:
int, float, str, list, tuple, set, dict
 Which are mutable and which are not?

5.
What is type casting?
 Difference between:
implicit vs explicit type conversion

6.
Explain Python operators:
Arithmetic
Logical
Comparison
Assignment
Membership
Identity
Give at least one real example for each.

7.
What is the difference between:
for loop
while loop
 When should you prefer one over the other?

8.
Explain break, continue, and pass with use cases.

9.
Explain difference between AND and & operator in interpreter

10.
Explain conditional statements:
if
if-else
if-elif-else
Also explain nested conditions with a real scenario.

## 1. Interpreted vs Compiled
- **Compiler**: Converts whole code before execution  
  - Example: C, C++
- **Interpreter**: Executes code line by line  
  - Example: Python  
- Python is **both interpreted and compiled** (internally converted to bytecode → executed by VM)

---

## 2. Mutable vs Immutable

### Mutable
- Can be changed after creation  
- Examples: `list`, `dict`, `set`

### Immutable
- Cannot be changed  
- Examples: `int`, `float`, `str`, `tuple`

---

## 3. Operators

### Assignment
- `=` → Assign value  
- `==` → Compare values  
- `is` → Check memory identity

### Arithmetic
- `+`, `-`, `*`, `/`, `//`, `%`, `**`

Example:
```python
a = 2
b = 1
c = a + b
print(c)
Logical
and, or, not

Example:

a = 5
print(a > 2 and a < 10)
Comparison
x = 5
print(x > 2)
Membership
a = [1, 2, 3]
print(2 in a)
Identity
a = [1, 2, 3]
b = a
print(a is b)


4. Type Casting
Convert one type to another
Types:
Implicit → Automatic
Explicit → Manual

Example:

a = int(input("Enter a: "))


5. Conditional Statements
Types:
if
if-else
if-elif-else
Example:
a = 2
if a > 3:
    print("a is greater than 3")
Example (age):
age = 15
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")


Multiple Conditions:
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


6. Nested If
num = -3

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")


7. Loops
For Loop
Used when number of iterations is known
for i in range(0, 5):
    print(i)
While Loop
Used when condition-based
a = 10
while a <= 10:
    print(a)
    a += 1

8. Loop Control Statements
break → Stops loop
continue → Skips iteration
pass → Does nothing


10. Match Case (Python)
a = 3
b = 5
c = int(input("Enter value: "))

match c:
    case 1:
        print(a)
    case 2:
        print(b)
    case _:
        print("Invalid")