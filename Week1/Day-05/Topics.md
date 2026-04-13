# 📘 Day 05 – Python Operators

## 🔹 What are Operators?

👉 Operators are symbols used to perform operations on variables and values.

Example:
```python
a = 5
b = 3
print(a + b)  # 8

## Types of Operators in Python
Arithmetic
Assignment
Comparison
Logical
Identity
Membership
Bitwise

## 🔹 1. Arithmetic Operators

Used for mathematical operations:

Operator	Meaning	        Example
+	        Addition	     5 + 2
-	        Subtraction	     5 - 2
*	        Multiplication	 5 * 2
/	        Division	     5 / 2
%	        Modulus	         5 % 2
**	        Power	         2 ** 3
//	        Floor Division	 5 // 2

##🔹 2. Assignment Operators

Used to assign values:

x = 5
x += 2   # x = x + 2
x -= 2
x *= 2
x /= 2

## 🔹 3. Comparison Operators

Used to compare values:

Operator	Meaning
==	        Equal
!=	        Not Equal
>	        Greater
<	        Less
>=	        Greater Equal
<=	        Less Equal

print(5 > 3)  # True

##🔹 4. Logical Operators

Used with conditions:

Operator	Meaning
and	         Both True
or	         Any True
not	         Reverse
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

## 🔹 5. Identity Operators

Check memory location:

a = [1,2]
b = a

print(a is b)      # True
print(a is not b)  # False

## 🔹 6. Membership Operators

Check presence:

a = [1,2,3,4]

print(2 in a)      # True
print(5 not in a)  # True


## 🔹 7. Bitwise Operators

Work on binary values:

Operator	Meaning
&	         AND
	
^	         XOR
~	         NOT
<<	         Left Shift
>>	         Right Shift
print(5 & 3)  # 1