# Day 03 

---

## 📌 Strings in Python

### Types:
- Single line string → "Hello" or 'Hello'
- Multi-line string → """Hello"""

### Example:
```python
name = "Suman"
msg = """This is
multi-line string"""


📌 Data Types

Python provides different ways to store multiple values.

🔹 1. List → []
Ordered
Mutable (changeable)
Allows duplicate values
Example:
lst = [1, 2, 3, 4]
lst[0] = 10
print(lst)

🔹 2. Tuple → ()
Ordered
Immutable (cannot change)
Faster than list
Example:
t = (1, 2, 3)
print(t[0])

🔹 3. Dictionary → {}
Key-value pairs
Unordered (in older versions)
Keys must be unique
Example:
d = {"name": "Suman", "age": 20}
print(d["name"])

🔹 4. Set → {}
Unordered
No duplicate values
Example:
s = {1, 2, 2, 3}
print(s)  # Output: {1, 2, 3}


Indexing
Indexing means accessing elements using position.

Example:
name = "Suman"

print(name[0])  # S
print(name[1])  # u

👉 Index starts from 0


📌 List vs Array
List:
Can store different data types
Slower
Flexible
Array:
Stores same type of data
Faster
Efficient


📌 NumPy (Important for ML 🔥)

NumPy is a library used for numerical operations.

🔹 Installation
pip install numpy

or

python -m pip install numpy
🔹 Import NumPy
import numpy as np
🔹 Create Array
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
🔹 Key Points
NumPy arrays are faster than lists
Store same data type
Used in Machine Learning & Data Science


📌 Python Array Module
import array
a = array.array('i', [1, 2, 3])

👉 'i' means integer type

📌 List vs NumPy Array
Feature	   List	    NumPy Array
Data Type  Mixed	Same type
Speed	   Slower	Faster
Usage	  General	ML/Data Science