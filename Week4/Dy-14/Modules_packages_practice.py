#modules and packages are used to organize code into manageable, reusable components.
'''Modules:- A module is a single file with a .py extension containing Python code (functions, classes, or variables). It allows you to group related code together for reuse in other programs.
Built-in Modules: Pre-installed with Python (e.g., math, os, sys, datetime).User-Defined Modules: Created by saving a .py file and importing it into another script.
User-Defined Modules: Created by saving a .py file and importing it into another script.
import module_name: Imports the entire module.
from module_name import function_name: Imports only a specific part.
import module_name as alias: Renames the module for easier reference.'''

'''Packages:- A package is a directory that contains multiple modules and typically a special file named __init__.py
A package is a directory that contains multiple modules and sub-packages. This creates a hierarchical structure for your code, preventing naming conflicts.
Collection of folders
How to Import: Use "dot notation" to access modules within a package, such as 
import package_name.module_name'''

#-----------------------------Modules---------------------------
#--------------------User defined-----------------
# Create a module mymodule.py
def greeting(name):
    print("hello",name)


import mymodule
mymodule.greeting(name="sumit")

from mymodule import greeting
greeting(name="suman")

from mymodule import *
add(a=2,b=3)
greeting(name="suman")

import mymodule
print(mymodule.person1["age"])

import mymodule as mx
mx.add(2,4)

#-----------------------built-in--------------------

import datetime
print(datetime.datetime.now())

import math
print(math.sqrt(64))
print(math.ceil(1.4)) # 2
print(math.floor(1.4)) # 1
print(math.pi)

import random
print(random.randint(1,2)) #both included
print(random.randrange(3,9))

#------------------------------------------Packages------------------------
# pip is a package manager for python packages
# Command to install and uninstall packages 
# pip install package_name
# pip uninstall package_name
# pip list - to list all the commands install on your system

#---------------------built in package-------------------------
# json - to work with json data , json is a syntax for storing and exchanging data

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)