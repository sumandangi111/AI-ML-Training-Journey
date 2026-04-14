# marks=float(input("Enter marks: "))
# if marks>=90:
#     grade="A"
# elif marks>=75:
#     grade="B"
# elif marks>=50:
#     grade="C"
# elif marks>=35:
#     grade="D"
# else:
#     grade="Fail"
# print("Grade :",grade)

print("Enter your marks")
a=float(input("Enter english marks = "))
b=float(input("Enter maths marks = "))
c=float(input("Enter science marks = "))
d=float(input("Enter hindi marks = "))
e=float(input("Enter social marks = "))

total= a+b+c+d+e

print("total marks obtained = ", total)

percentage = (total/5)

print("Percentage = ", percentage)

if percentage>=90:
    grade="A"
elif percentage>=75:
    grade="B"
elif percentage>=50:
    grade="C"
elif percentage>=35:
    grade="D"
else:
    grade="Fail"
print("Grade :",grade)