# 📘 File Handling & Exception Handling (Python Notes)

---

## 🔹 1. File Handling Basics

File handling allows us to work with files like reading, writing, and creating files.

### ✅ Common Functions

```python
open()   # Open a file
read()   # Read file content
write()  # Write into file
close()  # Close the file
```

---

## 🔹 2. File Modes

| Mode | Description                   |
| ---- | ----------------------------- |
| r    | Read (file must exist)        |
| w    | Write (overwrites file)       |
| x    | Create (error if file exists) |
| a    | Append (adds data to file)    |

---

## 🔹 3. Text vs Binary Modes

| Type   | Modes  |
| ------ | ------ |
| Text   | rt, wt |
| Binary | rb, wb |

---

## 🔹 4. Example: Reading a File

```python
f = open("test.txt", "r")
print(f.read())
f.close()
```

---

## 🔹 5. Common Errors in File Handling

### ❌ FileNotFoundError

Occurs when file does not exist:

```python
open("abc.txt", "r")
```

---

### ❌ FileExistsError

Occurs when using `x` mode and file already exists:

```python
open("test.txt", "x")
```

---

### ❌ UnsupportedOperation

Occurs when performing invalid operation:

```python
f = open("test.txt", "w")
f.read()  # ❌ Not allowed
```

---

## 🔥 6. Exception Handling

Exception handling prevents program crashes.

### ✅ Basic Syntax

```python
try:
    # risky code
except:
    # handle error
```

---

## 🔹 7. Handling Specific Errors

```python
try:
    f = open("test.txt", "x")
except FileExistsError:
    print("File already exists")
```

---

## 🔹 8. Using Exception Object

```python
try:
    f = open("test.txt", "w")
    print(f.read())
except Exception as e:
    print("Error:", e)
```

---

## 🔹 9. Best Practice: Using `with`

Automatically closes file.

```python
try:
    with open("test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

---

## 🔥 10. Key Concept Connection

| Action                 | Error                | Solution         |
| ---------------------- | -------------------- | ---------------- |
| open with x            | FileExistsError      | use try-except   |
| read in write mode     | UnsupportedOperation | use correct mode |
| read non-existing file | FileNotFoundError    | handle exception |

---