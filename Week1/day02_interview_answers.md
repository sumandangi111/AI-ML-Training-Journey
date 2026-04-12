# Day 02 - Interview Questions (Detailed Answers) 💼

---

## 🚀 print() – Questions

### ❓ Why does print("A", "B") give space automatically?
👉 Because `print()` uses a default separator `sep=" "` (space) between arguments.

---

### ❓ Difference between sep and end?
👉 `sep` → separates multiple values  
👉 `end` → what is printed at the end (default = newline)

Example:
print("A", "B", sep="-") → A-B  
print("Hello", end=" ") → stays on same line  

---

### ❓ print(5 + "5") vs print(str(5) + "5")?
👉 `5 + "5"` → ❌ Error (int + string not allowed)  
👉 `str(5) + "5"` → ✔ "55" (string concatenation)

---

### ❓ Why print() not used in production logging?
👉 Because:
- No log levels (info, error, warning)
- No timestamps
- Not scalable  

✔ Instead use logging module

---

### ❓ Difference in end behavior?
print("Hello", end="")
print("World")

👉 Output: HelloWorld  

Default:
👉 Hello  
👉 World  

---

### ❓ Why print() returns None?
👉 Because it only displays output, it doesn’t return any value.

---

## 🚀 input() – Questions

### ❓ Why input() always returns string?
👉 Because user input is treated as text by default.

---

### ❓ What if int(input()) gets invalid input?
👉 It throws ValueError  
Example: entering "abc" → crash

---

### ❓ Why input handling unsafe?
👉 Because user can enter:
- Wrong data
- Malicious input  

✔ Needs validation

---

### ❓ Difference:

a = input()
b = int(input())

👉 `a` → string  
👉 `b` → integer  

---

### ❓ Why input() is blocking?
👉 Program waits until user enters value → execution stops

---

### ❓ Multiple inputs in one line?
👉 Use:

a, b = map(int, input().split())


---

## 🚀 Variables – Questions

### ❓ Why no type declaration?
👉 Python is dynamically typed → type decided at runtime

---

### ❓ Reassign different type?

x = 10
x = "hello"

👉 Allowed → variable now refers to new object

---

### ❓ Variables store reference or value?
👉 Variables store **reference (address of object)**

---

### ❓ Why this behaves differently?

a = 5
b = a
a = 10

👉 `b` still 5  
👉 because `a` now points to new object

---

### ❓ Mutable vs Immutable?
👉 Mutable → can change (list)  
👉 Immutable → cannot change (int, string)

---

### ❓ Why naming important?
👉 Helps in:
- Debugging
- Readability
- Avoiding confusion in scope

---

## 🚀 Constants – Questions

### ❓ Does Python support constants?
👉 ❌ No strict constants  
👉 ✔ Convention (UPPERCASE)

---

### ❓ Why uppercase?
👉 To indicate value should not change

---

### ❓ What if changed?
👉 No error → Python allows it

---

### ❓ How to enforce constants?
👉 Use:
- Classes
- Read-only properties

---

### ❓ Why important in large systems?
👉 Avoid accidental changes  
👉 Improve maintainability

---

## 🚀 Literals – Questions

### ❓ Difference: 10, "10", 10.0?
👉 10 → int  
👉 "10" → string  
👉 10.0 → float  

---

### ❓ Why literals used directly?
👉 Quick and simple values without variable creation

---

### ❓ Types of literals?
👉 Numeric, String, Boolean, None

---

### ❓ "Hello" vs 'Hello'?
👉 No difference → both are strings

---

### ❓ Escape sequences?
👉 Special characters:
- \n → new line  
- \t → tab  

---

### ❓ Why literals immutable?
👉 Ensures data safety and optimization

---

## 🚀 Mixed / Thinking Questions

### ❓ Why this fails?

print("Age: " + 25)

👉 ❌ string + int not allowed  

✔ Fix:

print("Age:", 25)


---

### ❓ Safest way to take numeric input?
👉 Use validation:

try:
x = int(input())
except:
print("Invalid input")


---

### ❓ Why blindly trusting input() is bad?
👉 Can cause:
- Crashes
- Security issues  

---

### ❓ x = 10, y = 10 memory difference?
👉 Python may store both in same memory (optimization)

---

### ❓ Can variable start with number?
👉 ❌ No  
👉 Because Python syntax rules don’t allow it

---