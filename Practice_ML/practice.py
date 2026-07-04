'''
[45, 67, 89, 23, 90, 56]
Calculates:
Highest mark
Lowest mark
Average mark
Prints:
Highest: 90
Lowest: 23
Average: 61.67

l=[45, 67, 89, 23, 90, 56]
highest=l[0]
lowest=l[0]
average=0
n=len(l)
for i in l:
    average+=i
    if i>highest:
        highest=i
    elif i<lowest:
        lowest=i
print(highest)
print(lowest)
print((average)/n)'''

'''marks = [45, 67, 89, 23, 90, 56]
greater than 60
[67, 89, 90]

marks = [45, 67, 89, 23, 90, 56]
new=[]
for mark in marks:
    if mark>60:
        new.append(mark)
print(new)
'''

'''
marks = [45, 67, 89, 23, 90, 56]
Create three lists:
failed     = marks < 40
average    = 40 to 70
excellent  = > 70


marks = [45, 67, 89, 23, 90, 56]
failed=[]
average=[]
excellent=[]
for mark in marks:
    if mark<40:
        failed.append(mark)
    elif (mark>=40 and mark<=70):
        average.append(mark)
    else:
        excellent.append(mark)
print("Failed: ",failed)
print("Average: ",average)
print("Excellent: ",excellent)

print("Failed students: ",len(failed))
print("student score Average marks : ",len(average))
print("student perform Excellent: ",len(excellent))
'''

'''Number of students above average
Number of students below average
l=[45, 67, 89, 23, 90, 56]
highest=l[0]
lowest=l[0]
sum=0
n=len(l)
above_avg=0
below_avg=0
for i in l:
    sum+=i
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i
print(highest)
print(lowest)
average=sum/n
print(average)
for count in l:
    if count<average:
        below_avg+=1
    else:
        above_avg+=1
print("Number of students above average:",above_avg)
print("Number of students below average:",below_avg)'''

'''words = [
    "AI",
    "ML",
    "AI",
    "Python",
    "ML",
    "AI"
]
Create a program that outputs:
{
    "AI": 3,
    "ML": 2,
    "Python": 1
}

words = ["AI","ML","AI","Python","ML","AI"]
new={}
for word in words:
    if word not in new:
        new[word]=1
    else:
        new[word]+=1
print(new)'''

'''def calculate_stats(l):
    highest=l[0]
    lowest=l[0]
    n=len(l)
    total=0
    for i in l:
        total+=i
        if i>highest:
            highest=i
        elif i<lowest:
            lowest=i
    average=total/n
    return highest, lowest, average
l=[45, 67, 89, 23, 90, 56]
highest, lowest, average=calculate_stats(l)
print("Highest: ",highest)
print("lowest: ",lowest)
print("Average: ",average)

l = [10, 20, 30]
# print(l * 2)
import numpy as np
print(np.array(l) * 2)'''

'''Convert it into a NumPy array and print:
Original array
Array multiplied by 2
Array + 10
Array greater than 60
Expected idea:
[45 67 89 23 90 56]
[90 134 178 46 180 112]
[55 77 99 33 100 66]
[False True True False True False]

import numpy as np
marks = [45, 67, 89, 23, 90, 56]
arr=np.array(marks)
print(arr)
print(arr*2)
print(arr+10)
print(arr>60)'''

'''import numpy as np
marks = np.array([45, 67, 89, 23, 90, 56])
Find:
Marks greater than 60
Marks less than 50
Count of marks greater than 60
Average mark using NumPy
Highest mark using NumPy'''

import numpy as np
marks = np.array([45, 67, 89, 23, 90, 56])
print("Marks greater than 60:",marks>60)
print("Marks less than 50:",marks<50)
print("Count of marks greater than 60:",len(marks>60))
print("Average mark using NumPy:",sum(marks)/len(marks))
print("Highest mark using NumPy:",max(marks))