# 1.
new="banana"
l1={}
for i in new:
    if i in l1:
        l1[i]+=1
    else:
        l1[i]=1
print(l1)

# 2.
l1=[10,5,20,20,8]
larg=l1[0]
sec_lar=l1[0]
for i in range(0,len(l1)):
    if l1[i]>larg:
        sec_lar=larg
        larg=l1[i]
    elif l1[i]!=larg and l1[i]>sec_lar:
        sec_lar=l1[i]
print(larg)
print(sec_lar)

# 3.
n=123
num=n
result=0
while num>0:
    digit=num%10
    result=result*10+digit
    num=num//10
print(result)

# 5.
old=[1,2,2,3,1,4]
new=[]
for i in range(0,len(old)):
    if old[i] not in new:
        new.append(old[i])
print(new)

# 6.
l=[10,5,3,4,3,5,6]
new=[]
for i in range(0,len(l)):
    if l[i] not in new:
        new.append(l[i])
    else:
        print(l[i])
        break
#----------------------------
def func(num):
    if num==0 or num==1:
        return num
    else:
        return func(num-1)+func(num-2)
for i in range(8):
    print(func(i),end=" ")

#--------------------------------
# 4.
s = "({[]})"

stack = []
balanced = True

for ch in s:
    if ch == "(" or ch == "{" or ch == "[":
        stack.append(ch)

    elif ch == ")":
        if len(stack) == 0 or stack.pop() != "(":
            balanced = False
            break

    elif ch == "}":
        if len(stack) == 0 or stack.pop() != "{":
            balanced = False
            break

    elif ch == "]":
        if len(stack) == 0 or stack.pop() != "[":
            balanced = False
            break

if balanced and len(stack) == 0:
    print(True)
else:
    print(False)

# 7.
list1 = [1, 3, 5]
list2 = [2, 4, 6]

i = 0
j = 0
result = []

while i < len(list1) and j < len(list2):

    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

# Add remaining elements of list1
while i < len(list1):
    result.append(list1[i])
    i += 1

# Add remaining elements of list2
while j < len(list2):
    result.append(list2[j])
    j += 1

print(result)

# 8. 
import string

sentence = "Python is very powerful!"

# Remove punctuation
sentence = sentence.translate(str.maketrans("", "", string.punctuation))

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

# 9.
nums = [3, 0, 1]

n = len(nums)

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print(missing)

# 10.
arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)

arr = arr[-k:] + arr[:-k]

print(arr)