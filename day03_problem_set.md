Day 3
🚀 Data Types
❓ Why does Python not require explicit data type declaration but still enforces types at runtime?

👉 Python is dynamically typed, so you don’t declare types manually.
👉 However, it is strongly typed, meaning it strictly enforces type rules during execution and does not allow invalid operations between different types.

❓ What’s the real difference between type() and isinstance()?

👉 type() checks the exact type of an object.
👉 isinstance() checks type as well as inheritance (parent-child relationship).

❓ Why does this return True?
isinstance(True, int)

👉 Because in Python, bool is a subclass of int, so True is treated as 1.

❓ What happens internally when you do:
a = 5
b = 5.0

👉 a stores an integer object.
👉 b stores a float object.
👉 Both are stored differently in memory because integers are exact values while floats are approximate.

❓ Why is Python called strongly typed even though it’s dynamically typed?

👉 Because Python does not automatically convert incompatible types and throws errors instead, ensuring type safety.

❓ What exactly fails here and why?
"5" + 5

👉 This fails because Python does not allow operations between string and integer types without explicit conversion.

🚀 Mutable vs Immutable
❓ Why does this work differently?
a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)

👉 Both a and b point to the same list, so changes affect both.

a = 5
b = a
b = 10

👉 Here, b is reassigned to a new object, so a remains unchanged.

❓ Which data types are mutable and why does it matter in function calls?

👉 Mutable: list, dict, set
👉 Immutable: int, float, string, tuple
👉 Mutable objects can change inside functions, which may cause unexpected side effects.

❓ Why can strings not be modified in-place but lists can?

👉 Strings are immutable, so any change creates a new object.
👉 Lists are mutable, so they can be modified directly.

❓ What’s the hidden bug in modifying a list passed to a function?

👉 The original list gets modified unintentionally because functions receive references, not copies.

🚀 Type Conversion / Casting
❓ What’s the difference between implicit and explicit type conversion in Python?

👉 Implicit conversion is automatic (e.g., int → float).
👉 Explicit conversion is done manually using functions like int(), float(), str().

❓ Why does Python not automatically convert "5" to 5 in arithmetic operations?

👉 To avoid ambiguity and unexpected bugs, Python requires explicit conversion.

❓ What happens in:
int(5.9)

👉 Output is 5 because Python truncates the decimal part, causing data loss.

❓ Why is this dangerous?
float(input())

👉 If the user enters invalid input (like text), it causes a runtime error.

❓ What’s the difference between str(10) and "10" in memory behavior?

👉 "10" is created at compile time.
👉 str(10) is created at runtime.
👉 Both behave the same but are created differently.

🚀 Variables + Data Types
❓ If variables don’t have types, then what actually has the type?

👉 Objects have types, not variables. Variables only store references to objects.

❓ Why does this behave unexpectedly?
x = [1,2,3]
y = x
x = [4,5,6]

👉 y still points to the old list, while x now points to a new list.

❓ What is happening here?
a = [1,2]
b = a.copy()
a.append(3)
print(a)
print(b)

👉 b is a separate copy, so it remains unchanged.

❓ Why is shallow copy risky for nested data structures?

👉 Because inner objects are still shared between copies, leading to unexpected modifications.

❓ What problem does deep copy solve?

👉 It creates a completely independent copy, avoiding shared references.

🚀 Identity vs Equality
❓ Difference between:
a == b
a is b

👉 == checks value equality.
👉 is checks if both variables refer to the same object in memory.

❓ Why does this sometimes return True?
a = 100
b = 100

👉 Python caches small integers, so both refer to the same object.

❓ What is object identity in Python?

👉 It is the memory address of an object, which can be checked using id().

🚀 General Questions
❓ Why does this fail?
int("Hello")

👉 Because the string cannot be converted into an integer.

❓ Why does this work?
bool("False")

👉 Any non-empty string is considered True in Python.

❓ What’s the output and why?
print(type([]) == list)

👉 Output: True because the type of an empty list is list.

❓ Why are tuples faster than lists?

👉 Because tuples are immutable and optimized for performance.

❓ Why are sets unordered and how does that affect performance?

👉 Sets use hashing, so they don’t maintain order.
👉 This makes operations like search very fast (O(1)).