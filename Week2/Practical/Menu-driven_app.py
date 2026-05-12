while True:
    print("-----Menu-driven-application-----")
    print("1. Bill_split")
    print("2. Calculator")
    print("3. Stu_Marks_checker")
    print("4. Exit")

    choice=int(input("Enter choice :"))

    if choice==4:
        print("Program Ended!")
        break

    elif choice==1:
        Total_bill=float(input("Enter total bill amount:"))
        people=int(input("Enter number of people:"))
        per_person=Total_bill/people

        print("Total bill :",Total_bill)
        print("Each person should pay :",per_person)
        print("\n")
    elif choice==2:
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
        print("\n")
    
    elif choice==3:
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
        print("\n")

    else:
        print("Invalid choice!")
    
       