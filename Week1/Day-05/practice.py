# python
# Day 05 - Operators Practice

# Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)
print("Floor Division:", a // b)


# Assignment Operators
x = 5
x += 3
print("x after += :", x)

x *= 2
print("x after *= :", x)


# Comparison Operators
print("5 > 3:", 5 > 3)
print("5 == 3:", 5 == 3)
print("5 != 3:", 5 != 3)


# Logical Operators
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)


# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)


# Membership Operators
nums = [1, 2, 3, 4]

print("2 in nums:", 2 in nums)
print("5 not in nums:", 5 not in nums)


# Bitwise Operators
print("5 & 3:", 5 & 3)
print("5 | 3:", 5 | 3)
print("5 ^ 3:", 5 ^ 3)


# Real Example
age = 20

if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not Eligible")