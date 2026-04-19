'''1. Take input of two numbers and print:
sum
difference
product
division'''

a=int(input("Enter value of a ="))
b=int(input("Enter value of b ="))
print("Sum :",a+b)
print("Difference :",a-b)
print("Product :",a*b)
print("Division :",a/b)

''''2. Write a program to check:
if a number is even or odd
'''
n=int(input("Enter number ="))
if n%2==0:
    print("even")
else:
    print("odd")

'''3. Take a string input and:
print length
convert to uppercase
reverse it
'''
name=input("enter your name :")
print(len(name))
print(name.upper())
print(name[::-1])

'''4. Write a program using loops to:
print numbers from 1 to 100
print only even numbers
'''
for i in range(1,101):
    print(i)
for i in range(0,101,2):
    print(i)


'''5. Create a simple calculator using:
functions
user input
conditionals
'''
num1=float(input("Enter first number :"))
num2=float(input("Enter second number :"))
operator=input("Enter operator(+,-,*,**,/):")
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="**":
    result=num1**num2
elif operator=="/":
    if num2!=0:
        result=num1/num2
    else:
        result="Zero_division_error"
else:
    result="Invalid Operator"
print("Result :",result)


'''6. Build a unit converter:
km to meters
Celsius to Fahrenheit
'''
km = float(input())
print("Meters:", km * 1000)

c = float(input())
print("Fahrenheit:", (c * 9/5) + 32)


'''7. Write a program to check:
whether a student passed or failed
 (based on marks input)
'''
marks = int(input())

if marks >= 40:
    print("Pass")
else:
    print("Fail")

''''8. Build a basic expense splitter CLI app:
take total amount
number of people
print per person share
'''
amount = float(input())
people = int(input())

print("Each pays:", amount / people)

'''9. Write a match case condition:
that accepts a list
returns the maximum and minimum value
'''
lst = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

match lst:
    case []:
        print("Empty list")
    case _:
        print("Min =", min(lst), "Max =", max(lst))

'''10. Write a loop-based program:
print multiplication table of a number given by user
'''
num=int(input("Enter num :"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)