### Day 05
### String Behavior
❓ Why are strings immutable in Python? What problem does this design solve?

👉 Strings are immutable to ensure:

Memory efficiency (reuse objects)
Security (data cannot be changed accidentally)
Hashability (can be used as dictionary keys)
❓ What happens in memory?
s = "hello"
s = s + " world"

👉 A new string object is created
👉 Old "hello" remains unchanged

❓ Why is string concatenation in loops inefficient?

👉 Each concatenation creates a new object
👉 Leads to O(n²) time complexity

❓ Difference between:
s += "a"

and join()?
👉 += → creates new object repeatedly
👉 join() → builds string once → faster & efficient

### Indexing & Slicing
❓ Why does this not throw error?
s = "hello"
print(s[0:100])

👉 Python safely returns available range → "hello"

❓ What is negative indexing?

👉 Access elements from end
👉 -1 → last element

❓ What happens in:
s[::-1]

👉 Reverses the string

❓ Why slicing returns new object?

👉 Because strings are immutable
👉 Cannot modify original

❓ Difference between:
s[::2]
s[1::2]

👉 s[::2] → even index characters
👉 s[1::2] → odd index characters

### String Methods
❓ Why does replace() not modify original string?

👉 Strings are immutable → returns new string

❓ Difference between:
s.strip()
s.replace(" ", "")

👉 strip() → removes spaces from start & end
👉 replace() → removes all spaces

❓ Why does split() return list?

👉 Because it breaks string into multiple parts

❓ What if delimiter not found?

👉 Returns original string as single element list

❓ Why is join() faster?

👉 Avoids repeated memory allocation

### Comparison & Interning
❓ Why does this behave unexpectedly?
a = "hello"
b = "hello"
print(a is b)

👉 Due to string interning → same memory used

❓ What is string interning?

👉 Optimization where identical strings share memory

❓ Why not use is for string comparison?

👉 Because is checks memory, not value
👉 Always use ==

### Input + String Traps
❓ Why does this fail?
age = input()
print(age + 10)

👉 input() returns string → cannot add int

❓ Safe conversion?

👉 Use:

age = int(input())
❓ Why is .isdigit() not reliable?

👉 It fails for:

Negative numbers
Decimal values
### Escape Sequences & Formatting
❓ Difference between:
"Hello\nWorld"
r"Hello\nWorld"

👉 First → newline
👉 Second → prints raw text

❓ Why raw strings exist?

👉 To avoid escape sequence processing

❓ What if you forget escape \?

👉 Can cause:

Syntax error
Unexpected output
❓ Difference:
f"Value: {x}"
"Value: {}".format(x)

👉 f-string:

Faster
More readable
❓ Why f-strings preferred?

👉 Better performance and cleaner syntax

### Thinking Questions
❓ Why are strings hashable but lists are not?

👉 Strings are immutable → hashable
👉 Lists are mutable → cannot be hashed

❓ Why can strings be dictionary keys?

👉 Because they are immutable and hashable

❓ Why modifying string creates new object?

👉 Due to immutability

❓ Performance impact of large string operations?

👉 Can be slow due to repeated memory allocation
👉 Use join() for optimization