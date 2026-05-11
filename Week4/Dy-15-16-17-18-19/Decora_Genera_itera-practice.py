#---------------- iterator -------------------------------------
# used to iterate iterable objects like list, tuple, dict, set
iter(), next()

mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple:
    print(x)


#------------------ Generator ------------------------------------
#Generators are used in Python primarily to save memory and improve performance when handling large datasets, as they compute values on-the-fly (lazy evaluation) rather than storing entire sequences in RAM. They use the yield keyword to pause execution, allowing for efficient iteration through data without loading it all at once.
# Unlike return, which terminates the function, yield pauses it and can be called multiple times.

def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)

def new():
    return 1
    print("hello")
print(new())

def my_generator():
    yield 1
    yield 2
    yield 3
gen=my_generator()
print(next(gen))
gen.close()

#------------------------ Decorator -------------------------------
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello"

print(myfunction())