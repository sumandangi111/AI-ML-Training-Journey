'''The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.'''

# try:
#     print(x)
# except:
#     print("x is not defined")
# else:
#     print("there is no error in our code")
# finally:
#     print("always executed")

# raise an exception
# x=int(input("Enter number:"))
# if x<0:
#     raise Exception("Sorry,no number below 0")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")