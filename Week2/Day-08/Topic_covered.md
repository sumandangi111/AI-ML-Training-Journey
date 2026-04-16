# 📘 Python Notes – Patterns

---

## 🔹 What are Patterns?

Patterns are programs used to print shapes using loops (`for` / `while`).

👉 Helps improve:

* Logic building
* Loop understanding
* Nested loop concepts

---

## 🔹 1. Square Pattern

```python
n = 4

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

### Output:

```
* * * *
* * * *
* * * *
* * * *
```

---

## 🔹 2. Right Triangle Pattern

```python
n = 4

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
```

### Output:

```
*
* *
* * *
* * * *
```

---

## 🔹 3. Inverted Triangle

```python
n = 4

for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()
```

---

## 🔹 4. Number Pattern

```python
n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

### Output:

```
1
1 2
1 2 3
1 2 3 4
```

---

## 🔹 5. Pyramid Pattern

```python
n = 4

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))
```

---

## 🔹 Key Concept

👉 Patterns use **nested loops**:

* Outer loop → rows
* Inner loop → columns

---

## 🔹 Tips to Solve Patterns

1. Focus on rows first
2. Then columns
3. Identify relation between `i` and `j`