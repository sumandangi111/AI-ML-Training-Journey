new="banana"
l1={}
for i in new:
    if i in l1:
        l1[i]+=1
    else:
        l1[i]=1
print(l1)

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

n=123
num=n
result=0
while num>0:
    digit=num%10
    result=result*10+digit
    num=num//10
print(result)

old=[1,2,2,3,1,4]
new=[]
for i in range(0,len(old)):
    if old[i] not in new:
        new.append(old[i])
print(new)

l=[10,5,3,4,3,5,6]
new=[]
for i in range(0,len(l)):
    if l[i] not in new:
        new.append(l[i])
    else:
        print(l[i])
        break

def func(num):
    if num==0 or num==1:
        return num
    else:
        return func(num-1)+func(num-2)
for i in range(8):
    print(func(i),end=" ")