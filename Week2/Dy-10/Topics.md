# 📘 Python Notes – Lambda Functions (Basics)

---

# 🔹 1. Lambda Function

## ✅ Definition:

A **lambda function** is a **small anonymous (unnamed) function** used for short, one-line operations.

---

## 🔹 2. Syntax

```python
lambda arguments : expression
```

👉 It takes input → returns output (without using `return` keyword)

---

## 🔹 3. Basic Example

```python
add = lambda a, b: a + b
print(add(2, 3))   # Output: 5
```

---

## 🔹 4. Without Variable

```python
print((lambda x: x * 2)(5))   # Output: 10
```

---

## 🔹 5. Lambda with One Argument

```python
square = lambda x: x * x
print(square(4))   # 16
```

---

## 🔹 6. Lambda with Multiple Arguments

```python
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))   # 24
```

---

# 🔹 7. Why Use Lambda?

* Short and quick function
* No need to define using `def`
* Useful for temporary operations

---

# 🔹 8. Lambda vs Normal Function

| Feature | Lambda      | Normal Function |
| ------- | ----------- | --------------- |
| Name    | No          | Yes             |
| Syntax  | Short       | Longer          |
| Use     | Small tasks | Complex logic   |

---

# 🔹 9. Lambda with Conditional (Important)

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(5))   # Odd
```

---

# 🔹 10. Lambda with `map()`

## ✅ Definition:

`map()` applies a function to all elements of a list.

```python
nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))
print(result)   # [2, 4, 6, 8]
```

---

# 🔹 11. Lambda with `filter()`

## ✅ Definition:

`filter()` selects elements based on condition.

```python
nums = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)   # [2, 4]
```

---

# 🔹 12. Lambda with `sorted()`

```python
data = [(1, 3), (2, 1), (4, 2)]

print(sorted(data, key=lambda x: x[1]))
```

---

# 🔹 13. Limitations

* Only one expression allowed
* Not suitable for complex logic
* Less readable for beginners

---

# 🔹 14. When to Use

✔ Small calculations
✔ Temporary functions
✔ With `map()`, `filter()`, `sorted()`

---

# 🔹 15. When NOT to Use

❌ Complex logic
❌ Multiple statements

---