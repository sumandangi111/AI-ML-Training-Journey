# Day 04 Practice - Indexing, Slicing, Copying & Data Types

# 🔹 1. Indexing
a = [5, 10, 15, 20]
print("First element:", a[0])
print("Last element:", a[-1])


# 🔹 2. Mutable vs Immutable
# List (mutable)
lst = [1, 2, 3]
lst[0] = 10
print("Modified list:", lst)

# String (immutable)
s = "hello"
# s[0] = 'H'  # ❌ Error
print("String:", s)


# 🔹 3. String Slicing
a = "MONDAY"
print("Slice [3:5]:", a[3:5])
print("Slice [0:3]:", a[0:3])
print("Step slicing:", a[::2])
print("Reverse string:", a[::-1])


# 🔹 4. Copying (Shallow Copy)
a = [1, 2, 3]
b = a
a[0] = 10

print("Original list:", a)
print("Shallow copy:", b)


# 🔹 5. Deep Copy
import copy

a = [1, 2, 3]
b = copy.deepcopy(a)

a[0] = 100
print("Original list after change:", a)
print("Deep copied list:", b)


# 🔹 6. List Creation
a = [2, 3, 5]
print("List:", a)


# 🔹 7. String Formatting
name = "Suman"
age = 20
print(f"My name is {name} and age is {age}")


# 🔹 8. Escape Characters
print("Hello\nWorld")
print("Hello\tWorld")


# 🔹 9. String Methods
text = "hello world"
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())


# 🔹 10. Sets
s = {1, 2, 3}
s.add(4)
s.remove(2)
print("Set:", s)


# 🔹 11. Frozen Set
fs = frozenset([1, 2, 3])
print("Frozen set:", fs)
# fs.add(4)  # ❌ Error


# 🔹 12. Type Casting
a = 10
b = float(a)
c = str(a)

print("Float:", b)
print("String:", c)


# 🔹 13. Concatenation & Multiplication
a = "Hello"
b = "World"

print("Concatenation:", a + b)
print("Multiplication:", a * 3)


# 🔹 BONUS QUESTIONS

# Reverse a string using slicing
word = input("Enter a word: ")
print("Reversed:", word[::-1])


# Check mutable behavior
x = [1, 2]
y = x.copy()
x.append(3)

print("x:", x)
print("y:", y)