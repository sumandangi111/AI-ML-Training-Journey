# List
'''a=[1,2,2,3,4,5]
a.append(6)
a.insert(0,1)
b=[7,8,9,10]
a.extend(b)
print(a.pop()) #10
a.pop(0)
a.remove(5)#specific element
del a[1]
# del a #remove whole list
a.clear()
print(a)

c=a.copy()
print(c)

print(a.count(2))
print(a.index(2))

a.reverse()
print(a)
a.sort()
print(a)

#Tuple
a=(1,2,2,2,3,4,5)
print(a.count(2))
print(a.index(2))

#Dict
abc={
    "name":"suman",
    "age":22,
    "year":2026
}
abc.clear()
print(abc)

abc.pop("age") #remove specific key value
print(abc)
 
abc.popitem() #remove last key value
print(abc)

print(abc.get("age"))

print(abc.keys())
print(abc.values())
print(abc.items())

abc=("1.","2.","3.")
xyz=0
print(dict.fromkeys(abc,xyz))

abc["city"]="BIAORA"
abc["age"]=23
print(abc)
abc.update({"age":23})
print(abc)

#Set
old={1,2,3,4}
old.add(5)
new={6,7,8}
old.update(new)
old.remove(2)#give error if value dosn't exist
old.discard(3)#no error if value is not exist
old.clear()
del old
print(old)'''


#String
'''s="suman dangi"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s[0:2]) #string slicing

#strip()-remove whitespace from beginning and end
a=" Suman "
print(a.strip())
print(a.replace("an","it"))

#split()-convert string to list
a="Suman Dangi"
b=a.split(" ")
new=",".join(b)
print(new)'''

# concatenate string
a="suman"
b="dangi"
print(a+" "+b)