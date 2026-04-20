# Square Patterns

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()


# Triangle Patterns
'''1.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


'''2.
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5  
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

'''3.
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
'''
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''4.
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
'''
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

'''5.
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 
'''
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i,end=" ")
#     print()

'''6.
* 
* * 
* * * 
* * * * 
* * * * * 
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


'''7.
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''8.
* * * * * 
* * * * 
* * * 
* * 
* 
'''
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print("*",end=" ")
#     print()

'''9.
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''
# num=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

'''10.
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
'''
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''11.
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

'''12.
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range((i*2)-1):
#         print("*",end=" ")
#     print()

'''13.
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range((i*2)-1):
#         print("*",end=" ")
#     print()

# for i in range(4,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range((i*2)-1):
#         print("*",end=" ")
#     print()

#--------------------------------------------------------------------------------
# n=int(input("Enter number of rows :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#-----------------------------------
# n=int(input("Enter number of rows :"))
# ascii_value=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         alphabet=chr(ascii_value)
#         print(alphabet,end=" ")
#     ascii_value+=1
#     print()
'''
A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F''' 

#------------------------------------    
# n=int(input("Enter number of rows :"))
# ascii_value=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         alphabet=chr(ascii_value)
#         print(alphabet,end=" ")
#         ascii_value+=1
#     print()
'''
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S T U '''

#---------------------------------------
# n=int(input("Enter number of rows :"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()
'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
#-----------------------------------------
# n=int(input("Enter number of rows :"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()

'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''
#------------------------------------------
# n=int(input("Enter number of rows :"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("4",end=" ")
#     print()

'''
4 4 4 4 
4 4 4 
4 4 
4 
'''
#-------------------------------------------
# n=int(input("Enter number of rows :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
'''
#---------------------------------------------
# n=int(input("Enter number of rows :"))
# num=1
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(num,end=" ")
#     num+=1
#     print()

'''
Enter number of rows :7
            1 
          2 2 
        3 3 3 
      4 4 4 4 
    5 5 5 5 5 
  6 6 6 6 6 6 
7 7 7 7 7 7 7 
'''
#----------------------------------------------

'''
* * * * * * 1
* * * * * 1 2
* * * * 1 2 3 
* * * 1 2 3 4
* * 1 2 3 4 5
* 1 2 3 4 5 6
1 2 3 4 5 6 7
'''
# rows = int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     num=1
#     for j in range(rows,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num+=1
#     print()

#-------------------------------------------------------

rows = int(input("Enter the number of rows: ")) 
num=1
stop=2
for i in range(rows):
    for j in range(1,stop):
        print(num,end=" ")
        num+=1
    print()
    stop+=2

'''
Natural number pyramid
1 
2 3 4 
5 6 7 8 9 
10 11 12 13 14 15 16 
17 18 19 20 21 22 23 24 25 
26 27 28 29 30 31 32 33 34 35 36 
'''

#-------------------------------------------------------

rows = int(input("Enter the number of rows: ")) 
for i in range(1,rows+1):
    for j in range(1,i-1):
        print(j,end=" ")
        num+=1
    for j in range(i-1,0,-1):  
            print(j, end=" ")     
             
    print()


'''
Palindrom no. pyramid
'''