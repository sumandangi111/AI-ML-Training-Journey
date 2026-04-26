'''1. Calculator (Advanced)
Supports + - * / %
Handles invalid input using error handling
Allows continuous operations until user exits'''

# def calculator():
#     print("=== Advanced Calculator ===")
    
#     while True:
#         try:
#             num1 = float(input("Enter first number: "))
#             op = input("Enter operator (+, -, *, /, %): ")
#             num2 = float(input("Enter second number: "))

#             if op == '+':
#                 print("Result:", num1 + num2)
#             elif op == '-':
#                 print("Result:", num1 - num2)
#             elif op == '*':
#                 print("Result:", num1 * num2)
#             elif op == '/':
#                 if num2 == 0:
#                     print("Cannot divide by zero!")
#                 else:
#                     print("Result:", num1 / num2)
#             elif op == '%':
#                 print("Result:", num1 % num2)
#             else:
#                 print("Invalid operator!")

#         except ValueError:
#             print("Invalid input! Please enter numbers only.")

#         choice = input("Continue? (yes/no): ")
#         if choice.lower() != 'yes':
#             break

# calculator()

#----------------------------------------------------------------------

'''2. Expense Splitter CLI (Assignment Level)
Build a CLI app that:
Takes number of people
Accepts individual expenses
Splits fairly or unequally
Displays who owes whom'''


# def expense_splitter():
#     n=int(input("Enter number of people: "))
#     names=[]
#     expenses={}

#     for i in range(n):
#         name=input(f"Enter name {i+1}: ")
#         amount=float(input(f"Expense for {name}: "))
#         names.append(name)
#         expenses[name]=amount
#     total=sum(expenses.values())
#     equal_share=total/n

#     print("\n--------Split amount--------")
#     for name in names:
#         diff=expenses[name]-equal_share
#         if diff>0:
#             print(f"{name} should receive {diff:.2f}")
#         elif diff<0:
#             print(f"{name} should pay {-diff:.2f}")
#         else:
#             print(f"{name} nothing to pay or receive")
# expense_splitter()

#---------------------------------------------------------------------

'''3.Unit Converter (Advanced)
Create a converter that supports:
Temperature (C ↔ F)
Length (m ↔ km)
Weight (kg ↔ g)
 Use a menu-driven system
'''
# def unit_converter():
#     while True:
#         print("\n1. Temperature (C -> F)")
#         print("2. Length (m -> km)")
#         print("3. Weight (kg -> g)")
#         print("4. Exit")

#         choice=int(input("choose option: "))
#         if choice==1:
#             c=float(input("Enter Celcius: "))
#             print("Fahrenheit: ",(c*9/5)+32)
#         elif choice==2:
#             m=float(input("Enter meters: "))
#             print("Kilometers : ",m/1000)
#         elif choice==3:
#             kg=float(input("Enter kg: "))
#             print("Grams:",kg*1000)
#         elif choice==4:
#             break
#         else:
#             print("Invalid choice!")
# unit_converter()

#-------------------------------------------------------------------

'''4. Student Marks Analyzer
Program should:
Accept marks for multiple students
Store in dictionary
Calculate:
     Average
     Highest scorer
     Pass/Fail status
'''
# def student_analyzer():
#     students={}
#     n=int(input("Enter number of stuents: "))
#     for _ in range(n):
#         name=input("Enter name: ")
#         marks=float(input("Enter marks: "))
#         students[name]=marks
    
#     avg=sum(students.values())/n
#     topper=max(students,key=students.get)

#     print("\nAverage Marks:",avg)
#     print("Topper:",topper)

#     print("\nPass/Fail Status:")
#     for name,marks in students.items():
#         status="Pass" if marks>=40 else "Fail"
#         print(name,":",status)

# student_analyzer()

'''5. Number Guessing Game (Enhanced)
Random number generation
Limited attempts
Give hints (too high / too low)
Track score
'''
import random
def guessing_game():
    number=random.randint(1,100)
    attempts=5
    print("Guess the number (1-100)")
    for i in range(attempts):
        guess=int(input("Enter guess: "))

        if guess==number:
            print("Correct! you win")
            return
        elif guess>number:
            print("Too high!")
        else:
            print("Too low!")
    print("You lost! Number was:",number)

guessing_game()

#--------------------------------------------------------------------

'''6. Password Strength Checker
Check password based on:
Length ≥ 8
Contains uppercase, lowercase
Contains number and special character
Return Weak / Medium / Strong
'''