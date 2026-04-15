# 📘 Python Notes – Conditionals, Loops & Scope


## 🔹 1. Conditional Statements

Conditional statements are used to make decisions in a program.

### ✅ Types:

* `if`
* `if-else`
* `if-elif-else`
* Nested if

### 📌 Example:

```python
a = 10
b = 20

if a > b:
    print("a is greater")
else:
    print("b is greater")
```

---

## 🔹 2. Short-Hand If-Else (Ternary Operator)

```python
a = 10
b = 20

print("A") if a > b else print("B")
```

---

## 🔹 3. Pass Statement

Used when a statement is required but you don’t want any code to execute.

```python
if True:
    pass
```

---

## 🔹 4. Match Case (Switch Alternative)

```python
a = 3

match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
```

---

## 🔹 5. Loops

Loops are used to repeat code.

### ✅ Types:

* `for loop`
* `while loop`

---

### 🔸 While Loop

```python
a = 1

while a <= 5:
    print(a)
    a += 1
```

---

### 🔸 For Loop

```python
for i in range(5):
    print(i)
```

---

## 🔹 6. Range Function

```python
range(start, stop, step)
```

### Example:

```python
for i in range(0, 10, 2):
    print(i)
```

---

## 🔹 7. Do-While Concept

Python does not support do-while directly.

```python
while True:
    print("Runs at least once")
    break
```

---

## 🔹 8. Scope of Variables

Types:

* Local
* Global
* Non-local

---

## 🔹 9. Global Keyword

```python
x = 10

def change():
    global x
    x = 20

change()
print(x)
```

---

## 🔹 10. Nonlocal Keyword

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
```

---

## 🔹 11. LEGB Rule

* L → Local
* E → Enclosing
* G → Global
* B → Built-in

---

# 🚀 Summary

* Conditionals → Decision making
* Loops → Repetition
* Range → Sequence generation
* Match-case → Multiple conditions
* Scope → Variable visibility
* LEGB → Variable lookup order

---
