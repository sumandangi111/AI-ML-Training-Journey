# Conditional

# 1. Swap two numbers
a=2
b=4
a,b=b,a
print("a :",a)
print("b :",b)

# 2.Check the number is odd or even
a=int(input("Enter value of a ="))
if(a%2==0):
    print("Even")
else:
    print("odd")

# 3.Check the number is +ve or -ve
a=int(input("Enter value of a ="))
if a==0:
    print("no. is 0")
elif(a>0):
    print("a is +ve")
else:
    print("a is -ve")

# Leap year
year=int(input("Enter year :"))
if((year%4==0 and year%100!=0) or year%400==0):
    print("Leap year")
else:
    print("not a leap year")

# Largest among 3 no.
a=3
b=4
c=1
if(a>b)and(a>c):
    print(a,"is alrgest")
elif(b>a)and(b>c):
    print(b," is greatest")
else:
    print(c,"is greatest")

# Prime or not
num = int(input("Enter a number here: "))
if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
    
