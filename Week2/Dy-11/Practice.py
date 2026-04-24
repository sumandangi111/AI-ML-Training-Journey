# def student_info(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)

# # Calling function
# student_info("Suman", 21 ,"BCA")

# def student_info(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)

# # Calling with keywords
# student_info(age=21, name="Suman", course="BCA")

# def total_marks(*marks):
#     total = 0
#     for m in marks:
#         total += m
#     print("Total Marks:", total)

# # Calls
# total_marks(80, 90, 70)
# total_marks(50, 60)

# def complete_function(a, b, c=10, *args, **kwargs):
#     print("Positional:", a, b)
#     print("Default:", c)
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# complete_function(
#     1, 2,                # positional
#     5,                   # default overridden
#     100, 200, 300,       # *args
#     name="Suman", age=21 # **kwargs
# )

# def func():
#     x = 10
#     print(x)
# func()

# x = 10
# def func():
#     print(x)
# func()
#  print(x)

x = 10

# def change():
#     global x
#     x = 20

# change()
# print(x)

# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x = 20
#     inner()
#     print(x)
# outer()
# print(x)


students = [
    {"name": "Suman", "marks": 85},
    {"name": "Rahul", "marks": 75},
    {"name": "Anita", "marks": 90}
]

sorted_students = sorted(students, key=lambda x: x["marks"])

for s in sorted_students:
    print(s)