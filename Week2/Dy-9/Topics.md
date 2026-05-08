# 📘 Functions in Python

## 🔹 What is a Function?
A **function** is a block of reusable code used to perform a specific task.

### 👉 Benefits:
- Code reusability  
- Reduces repetition  
- Improves readability  

---

## 🔹 Basic Syntax

```python
def function_name():
    # code
✅ Example:
def test():
    print("Testing")

test()   # function call


🔹 Parameters vs Arguments
Term	    Meaning
Parameter	Variable in function definition
Argument	Value passed during function call


✅ Example:
def add(a, b):   # a, b → parameters
    c = a + b
    print(c)

add(2, 3)   # 2, 3 → arguments

Output:

5


🔥 Types of Parameters in Python

There are 5 types of arguments:

1️⃣ Positional Arguments

Values are assigned based on position.

def test(a, b):
    print(a, b)

test(10, 20)

Output:

10 20

❗ Order matters.


2️⃣ Keyword Arguments

Values are assigned using parameter names.

def test(a, b):
    print(a, b)

test(b="Suman", a="Megha")

Output:

Megha Suman

✔ Order does NOT matter


3️⃣ Arbitrary Arguments (*args)

Used when number of arguments is unknown. Stored as a tuple.

def test(*a):
    print(a)

test(1, 2, 3, 4)

Output:

(1, 2, 3, 4)
Access specific value:
def test(*a):
    print(a[2])

test(10, 20, 30, 40)

Output:

30

4️⃣ Default Arguments

Parameter has a default value.

def test(a="Suman"):
    print(a)

test()

Output:

Suman
Override default:
test("Rahul")

Output:

Rahul

5️⃣ Keyword Arbitrary Arguments (**kwargs)

Accepts multiple keyword arguments. Stored as a dictionary.

def test(**a):
    print(a)

test(name="Suman", age=21)

Output:

{'name': 'Suman', 'age': 21}
Access values:
def test(**a):
    print(a["name"])

test(name="Suman", age=21)

Output:

Suman


🔹 Important Notes
*args → tuple
**kwargs → dictionary

✔ Correct Order of Parameters:
def func(positional, default, *args, **kwargs):
    pass

🔹 Key Points to Remember
Function = reusable block of code
Parameters = variables
Arguments = actual values

5 Types of Arguments:
Positional
Keyword
*args
Default
**kwargs