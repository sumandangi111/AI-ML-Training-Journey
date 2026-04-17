## OPERATORS
Core Operator Understanding

## Q1. What is operator precedence? Give a real example where it changes output.
Answer:
Operator precedence defines the order in which operations are evaluated.

Example:

result = 10 + 2 * 3   # 16

* has higher precedence than +, so:

10 + (2 * 3) = 16

If changed:

result = (10 + 2) * 3  # 36

## Q2. Explain associativity with example: 2 ** 3 ** 2
Answer:
Associativity defines direction of evaluation when operators have same precedence.

Exponentiation is right-associative:

2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512

## Q3. Difference between == and is (memory explanation)
Answer:

== → compares values
is → compares memory identity
a = [1,2]
b = [1,2]

a == b  # True (same value)
a is b  # False (different objects)

## Q4. Why Python allows chained comparisons like 1 < x < 5 but C/Java don’t?
Answer:
Python evaluates it as:

(1 < x) and (x < 5)

Efficient and avoids repeating x.
C/Java evaluate left to right → incorrect logic.

🔷 Arithmetic Operators

## Q5. Floor division with negatives: -5 // 2
Answer:
Floor division rounds towards negative infinity:

-5 // 2 = -3

## Q6. Why modulo behaves differently in Python vs C?
Answer:
Python ensures:

(a // b) * b + (a % b) = a

So result has same sign as divisor.

-5 % 2 = 1

C keeps sign of dividend → different result.

## Q7. Why 0.1 + 0.2 != 0.3?
Answer:
Due to floating-point precision (binary representation):

0.1 + 0.2 = 0.30000000000000004

## Q8. Difference between / and //
Answer:

/ → float division
// → floor division (int or float)
🔷 Assignment Operators

## Q9. Difference: a += b vs a = a + b
Answer:

For mutable objects → modifies in-place
For immutable objects → creates new object

## Q10. What happens here?

a = [1,2]
b = a
a += [3]
print(b)

Answer:
Output:

[1,2,3]

Because list is mutable and modified in-place.

## Q11. What is chained assignment? Why dangerous?
Answer:

x = y = []

Both refer to same object → modifying one affects both.

🔷 Comparison Operators

## Q12. Explain chained comparison: a < b < c
Answer:
Equivalent to:

(a < b) and (b < c)

## Q13. Why comparing different data types is risky?
Answer:
May raise error:

5 < "10"  # TypeError

## Q14. What if objects don’t support comparison?
Answer:
Python raises TypeError.

🔷 Identity vs Equality

## Q15. When use is instead of ==?
Answer:
Use is for:

None
singleton objects

## Q16. Why this may return True?

a = 100
b = 100
print(a is b)

Answer:
Due to integer interning (small integers cached).

## Q17. Object identity vs value?
Answer:

Identity → memory address
Value → actual data
🔷 Logical Operators

## Q18. Short-circuiting?
Answer:
Evaluation stops early:

False and (1/0)  # no error

## Q19. Output

5 and 0   # 0
0 or 5    # 5

## Q20. Why and/or return operands?
Answer:
They return last evaluated value, not boolean.

## Q21. Practical use
Answer:

name = input() or "Guest"
🔷 Bitwise Operators

## Q22. Difference & vs and
Answer:

& → bitwise
and → logical

Q23. Explain

5 & 3 = 1
5 | 3 = 7
5 ^ 3 = 6

## Q24. Left shift / Right shift
Answer:

<< → multiply by 2
>> → divide by 2

## Q25. Real-world usage
Answer:

networking
encryption
flags handling
🔷 Membership Operators

## Q26. Difference: list vs string
Answer:

list → checks element
string → checks substring

## Q27. Time complexity
Answer:

list → O(n)
set/dict → O(1)

## Q28. Why set faster?
Answer:
Uses hashing

🔷 Operator Precedence

## Q29. Output

not True == False  # True

## Q30. Why dangerous?

a = True and False or True  # True

Confusing precedence → leads to bugs.

## Q31. Role of parentheses
Answer:
Explicit control of evaluation order.

🔷 Edge Cases
True + True → 2
[] or "Hello" → "Hello"
"" and "World" → ""
10 == 10.0 → True
5 < 10 > 5 → True
🔷 Real-World

## Q32. Misuse of is causes bugs?
Comparing values instead of identity → unpredictable behavior.

## Q33. Short-circuit prevents errors?
Avoids unsafe evaluation:

if x and x[0]:

## Q34. Mutable vs immutable behavior?
Mutable → in-place change
Immutable → new object

## Q35. Why precedence important?
Wrong conditions → logical bugs

🔷 CONDITIONAL STATEMENTS
If-Else Basics

## Q36. What does Python evaluate in if?
Answer:
Any expression → converted to truthy/falsy

## Q37. Why this works?

if 5:

Because non-zero → True

## Q38. Falsy values

0, None, False, "", [], {}, set()
🔷 Logical Thinking

## Q39. if x vs if x is True
Answer:

if x → checks truthiness
if x is True → strict boolean

## Q40. Why if x == True is wrong?
Redundant and unsafe.

## Q41. What happens?

if "":

Does not execute (empty string is False)

🔷 Flow Control

## Q42. if vs elif vs else
Only one block executes.

## Q43. Why only one executes?
Because evaluation stops after first True.

## Q44. Multiple if instead of elif?
All conditions checked → multiple blocks may run.

🔷 Nested Conditions

## Q45. Why bad?
Hard to read, maintain.

## Q46. How reduce complexity?

use logical operators
early return

## Q47. Difference

if a:
  if b:

vs

if a and b:
🔷 Short-Circuit

## Q48. Why no crash?

if True or (1/0):

Second condition not evaluated.

🔷 Operator + If

## Q49. What’s wrong?

if x == 10 or 20:

Always True.

## Q50. Correct way

if x == 10 or x == 20

or

if x in (10, 20)

## Q51. Why wrong?

x == (10 or 20)  # becomes x == 10
🔷 Membership vs Identity

## Q52. in vs is

in → membership
is → identity

## Q53. When use is?
Only for None, singletons.

🔷 Edge Outputs
if None → No
if [] → B
if "False" → True
if 0 → World
🔷 Ternary Operator

## Q54. What is it?

x = 10 if cond else 20

## Q55. Difference from normal if
Shorter, but less readable.

## Q56. When NOT to use?
Complex conditions.

🔷 Advanced

## Q57. Can if work without boolean?
Yes → truthy/falsy concept.

## Q58. Internal evaluation?
Uses bool() conversion.

## Q59. Non-boolean condition?
Converted using truth value testing.

## Q60. Assignment inside if?
Yes using walrus operator:

if (n := len([1,2,3])) > 2: