# Day 02 Practice - Variables, Literals & Input/Output

# 1. Create variables and print
name = "Suman"
age = 20
city = "Indore"
print("Name:", name, "Age:", age, "City:", city)


# 2. Take user input and print greeting
user_name = input("Enter your name: ")
print("Hello", user_name)


# 3. Take a number and print double
num = int(input("Enter a number: "))
print("Double:", num * 2)


# 4. Different literals
a = 10        # integer
b = 3.14      # float
c = "Python"  # string
d = True      # boolean
print(a, b, c, d)


# 🔹 Medium Level

# 5. Take two numbers and perform operations
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)


# 6. Age after 5 years
age = int(input("Enter your age: "))
print("After 5 years, your age will be", age + 5)


# 7. Area of circle using constant
PI = 3.14
radius = float(input("Enter radius: "))
area = PI * radius * radius
print("Area of circle:", area)


# 8. Swap two variables
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

a, b = b, a
print("After swapping:", "a =", a, ", b =", b)


# 🔹 Thinking Level

# 9. Name and age sentence
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("My name is", name, "and I am", age, "years old")


# 10. Average of 3 numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

avg = (n1 + n2 + n3) / 3
print("Average:", avg)


# 11. String to integer conversion
num_str = input("Enter a number: ")
num_int = int(num_str)
print("After adding 10:", num_int + 10)


# 12. Data type check
value = input("Enter something: ")
print("Before casting:", type(value))

value_int = int(value)
print("After casting:", type(value_int))


# 🔹 Bonus

# 13. Square and cube
num = int(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)


# 14. Uppercase conversion
text = input("Enter text: ")
print("Uppercase:", text.upper())


# 15. Formatted output
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum of", a, "and", b, "is", a + b)