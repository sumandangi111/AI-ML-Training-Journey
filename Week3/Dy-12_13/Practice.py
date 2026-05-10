# File handling
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists'''

#Create a sample file if it doesn't exist
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: World\n")
    f.write("Line 3: File Handling\n")

#Now read it
with open("sample.txt", "r") as f:
    print(f.read())

f=open("sample.txt","r")
print(f.read())
f.close()

with open("sample.txt", "r") as f:
    print(f.readline())
    print(f.readlines())

with open("sample.txt", "r") as f:
    print(f.read(5)) #read number of characters

with open("sample.txt", "r") as f:
    for x in f:
        print(x)


with open("sample.txt", "w") as f:
    f.write("new content\n")

with open("sample.txt","r") as f:
    print(f.read())

with open("sample.txt", "a") as f:
    f.write("new content\n")

with open("sample.txt","r") as f:
    print(f.read())

f=open("new.txt","x")
with open("new.txt","w") as f:
    f.write("this is a new file!")
with open("new.txt","r") as f:
    print(f.read())

#os is a inbuilt module which provide functions to interact with the os
import os
# os.remove("new.txt")
if os.path.exists("new.txt"):
    print("file exists")
else:
    print("file not exists")

import os
os.rmdir("no")  #to delete folder 
