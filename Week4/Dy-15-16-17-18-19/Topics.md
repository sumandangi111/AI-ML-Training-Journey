'''Basic OOP 
● Advanced OOP 
● Decorators 
● Generators & iterators 
● Context managers 
● Logging 
● Environment configuration (.env) 
● API handling basics 
● Intro to async programming'''

# Object Oriented Programming (OOP) & Python Notes

## What is OOP?

Object Oriented Programming (OOP) is a programming approach based on objects and classes.

### Advantages of OOP

* Memory saving
* Increases efficiency
* Reusability of code
* Better organization of programs

---

# Object and Class

## Object

An object is an instance of a class.

Example:

```python
car1 = Car()
```

## Class

A class is a blueprint of code.
It is a collection of:

* Variables
* Functions / Methods

Memory is not allocated to the class until an object is created.

### Syntax of Class

```python
class ClassName:
    # statements
```

### Syntax of Object

```python
object_name = ClassName()
```

### Example

```python
class Cal:
    def add(self, a, b):
        c = a + b
        print(c)

obj = Cal()
obj.add(2, 4)
```

---

# Four Pillars of OOP

1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphism

---

# Inheritance

Inheritance allows one class to acquire properties and methods of another class.

## Types of Inheritance

1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hybrid Inheritance
5. Hierarchical Inheritance

---

## 1. Single Inheritance

One child class inherits from one parent class.

```python
class A:
    pass

class B(A):
    pass
```

---

## 2. Multilevel Inheritance

A class inherits from another derived class.

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

## 3. Multiple Inheritance

One child class inherits from multiple parent classes.

```python
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass
```

---

## 4. Hierarchical Inheritance

Multiple child classes inherit from one parent class.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```

---

## 5. Hybrid Inheritance

Combination of two or more types of inheritance.

---

# Encapsulation

Encapsulation means combining data and methods into one unit (class).

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

# Abstraction

Abstraction means showing only essential features and hiding implementation details.

---

# Polymorphism

Polymorphism means:

**Poly = Many**

**Morphism = Forms**

It allows the same method name to behave differently.

## Method Overloading

Same method name with different parameters.

## Method Overriding

Child class provides a different implementation of a parent class method.

### Example of Method Overriding

```python
class A:
    def show(self):
        print("Parent method")

class B(A):
    def show(self):
        print("Child method")

obj = B()
obj.show()
```

---

# Constructor in Python

## **init**() Constructor

The `__init__()` method is called automatically when an object is created.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

# self Keyword

* `self` refers to the current object.
* It stores the address/reference of the current object.
* `self` is not a keyword.

Example:

```python
class Demo:
    def show(self):
        print("Hello")
```

---

# Iterators

An iterator is an object that contains a countable number of values and can be traversed.

List, tuple, dictionary, and set are iterable objects.

They use:

* `iter()` → returns iterator object
* `next()` → returns next value

### Example

```python
mytuple = ("apple", "banana")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
```

---

# Generators

A generator is a special type of function that returns an iterator object.

It uses the `yield` keyword.

### Example

```python
def myfunc():
    yield "Hello"
    yield 51

x = myfunc()

for z in x:
    print(z)
```

---

# Decorators

Decorators allow you to add extra behavior to an existing function or class without changing its source code.

### Syntax

```python
@decorator_name
```

---

# Context Manager

Context managers are used for file handling using `with` keyword.

### Example

```python
with open("file.txt", "r") as file:
    data = file.read()
```

---

# Logging in Python

Logging is used to store logs/events shown in the terminal.

### Example

```python
import logging

logging.warning("This is a warning")
```

---

# API Configuration

API configuration is used to connect applications with external services.

---

# Environment Configuration (.env)

Environment variables are stored in `.env` files.

Example:

```env
API_KEY=123456
```

---

# Asynchronous Programming (Async Programming)

Async programming allows multiple tasks to run efficiently without waiting for each task to finish completely.

---

# Virtual Environment

A virtual environment is used to create an isolated Python environment.

## Create Virtual Environment

```bash
python -m venv env_name
```

## Activate Virtual Environment

### Linux / Mac

```bash
source env_name/bin/activate
```

### Windows

```bash
env_name\Scripts\activate
```

## Deactivate Virtual Environment

```bash
deactivate
```

---

# Quick Revision Points

## OOP

* Object → Instance of class
* Class → Blueprint of code
* OOP improves efficiency and memory management

## Four Pillars

* Inheritance
* Encapsulation
* Abstraction
* Polymorphism

## Important Python Concepts

* Constructor → `__init__()`
* `self` → Current object reference
* Iterator → `iter()` and `next()`
* Generator → Uses `yield`
* Decorator → Adds extra functionality
* Context Manager → Uses `with`
* Virtual Environment → `python -m venv`
