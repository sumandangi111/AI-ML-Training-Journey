# 📘 Python Basics – Indexing, Slicing, Copying & Data Types

## 🔹 1. Indexing
- Indexing is used to access elements in a sequence (like list, string).
- Index starts from **0**

```python
a = [5, 10, 15]
print(a[0])  # Output: 5
```

👉 Index = position of element

---

## 🔹 2. Mutable vs Immutable

| Type        | Mutable | Example        |
|------------|--------|---------------|
| List       | ✅ Yes | `[1,2,3]`     |
| String     | ❌ No  | `"hello"`     |
| Tuple      | ❌ No  | `(1,2,3)`     |
| Set        | ✅ Yes | `{1,2,3}`     |
| Dictionary | ✅ Yes | `{key:value}` |

👉 **Mutable** → Can change  
👉 **Immutable** → Cannot change  

---

## 🔹 3. String is Immutable

```python
a = "hello"
# a[0] = 'H' ❌ Error
```

---

## 🔹 4. String Slicing

👉 Extract part of string

```python
a = "MONDAY"
print(a[3:5])  # Output: "DA"
```

### 📌 Syntax:
```python
string[start : stop : step]
```

- `start` → starting index  
- `stop` → ending index (excluded)  
- `step` → jump  

---

## 🔹 5. Slicing Examples

```python
a = "MONDAY"

print(a[0:3])   # MON
print(a[::2])   # MNA
print(a[::-1])  # YADNOM (reverse)
```

---

## 🔹 6. Copying in Python

### ✅ Shallow Copy
- Copies reference
- Changes affect both

```python
a = [1,2,3]
b = a
a[0] = 10

print(b)  # [10,2,3]
```

---

### ✅ Deep Copy
- Creates new memory
- Changes do NOT affect original

```python
import copy

a = [1,2,3]
b = copy.deepcopy(a)

a[0] = 10
print(b)  # [1,2,3]
```

---

## 🔹 7. List Creation

```python
a = [2, 3, 5]
```

- Comma-separated values
- Stored inside `[ ]`

---

## 🔹 8. String Formatting

```python
name = "Suman"
age = 20

print(f"My name is {name} and age is {age}")
```

👉 Used to format strings dynamically

---

## 🔹 9. Escape Characters

| Character | Meaning        |
|----------|----------------|
| `\n`     | New line       |
| `\t`     | Tab space      |

```python
print("Hello\nWorld")
```

---

## 🔹 10. String Methods

```python
a = "hello world"

print(a.upper())     # HELLO WORLD
print(a.lower())     # hello world
print(a.title())     # Hello World
```

---

## 🔹 11. Sets

- Unordered collection
- No duplicates
- Mutable

```python
s = {1,2,3}
s.add(4)
s.remove(2)
```

---

## 🔹 12. Frozen Set

- Immutable version of set

```python
fs = frozenset([1,2,3])
# fs.add(4) ❌ Error
```

---

## 🔹 13. Type Casting

```python
a = 10

b = float(a)   # 10.0
c = str(a)     # "10"
```

---

## 🔹 14. Concatenation & Multiplication

```python
a = "Hello"
b = "World"

print(a + b)   # HelloWorld
print(a * 3)   # HelloHelloHello
```

---

# 🚀 Summary
- Indexing → access elements  
- Slicing → extract data  
- Mutable vs Immutable → important concept  
- Shallow vs Deep Copy → memory concept  
- Strings → immutable  
- Sets → unique values  
- Type casting → data conversion  
