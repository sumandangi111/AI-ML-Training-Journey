# 📦 Modules & Packages in Python (Complete Notes with Examples)

---

# 🔹 What is a Module?

A **module** is a single `.py` file containing:

* functions
* variables
* classes

👉 Used for **code reuse & organization**

---

## Example: Custom Module

```python
# my_module.py
def add(a, b):
    return a + b
```

### 🔹 Using Module

```python
import my_module
print(my_module.add(2, 3))
```

---

## 🔹 Import Styles

```python
import my_module
from my_module import add
import my_module as mm
```

---

# 🔹 What is a Package?

A **package** is a folder containing multiple modules.

---

## Structure

```
calculator/
│
├── __init__.py
├── add.py
├── sub.py
```

---

## Example

```python
# add.py
def add(a, b):
    return a + b
```

```python
# main.py
from calculator.add import add
print(add(5, 2))
```

---

# 🔹 Built-in Modules (Important with Examples)

---

## 1. math

```python
import math
print(math.sqrt(16))
print(math.factorial(5))
```

---

## 2. random

```python
import random
print(random.randint(1, 10))
print(random.choice([1,2,3]))
```

---

## 3. datetime

```python
import datetime
print(datetime.datetime.now())
```

---

##  4. time

```python
import time
print(time.time())
time.sleep(1)
```

---

## 5. os

```python
import os
print(os.getcwd())
```

---

## 6. sys

```python
import sys
print(sys.version)
```

---

## 7. json

```python
import json
data = {"name": "Suman"}
print(json.dumps(data))
```

---

## 8. csv

```python
import csv

with open("file.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
```

---

## 9. re (Regex)

```python
import re
print(re.findall(r"\d+", "abc123"))
```

---

## 10. collections

```python
from collections import Counter
print(Counter([1,1,2,3]))
```

---

## 11. itertools

```python
import itertools
for i in itertools.count(1):
    if i > 3:
        break
    print(i)
```

---

## 12. sqlite3

```python
import sqlite3
conn = sqlite3.connect("test.db")
```

---

## 13. threading

```python
import threading

def task():
    print("Thread running")

t = threading.Thread(target=task)
t.start()
```

---

## 14. urllib

```python
import urllib.request
res = urllib.request.urlopen("https://example.com")
print(res.status)
```

---

## 15. logging

```python
import logging
logging.warning("Warning message")
```

---

# 🔹 External Packages (Important)

---

## 1. numpy

```python
import numpy as np
print(np.array([1,2,3]))
```

---

## 2. pandas

```python
import pandas as pd
df = pd.DataFrame({"A":[1,2]})
print(df)
```

---

## 3. matplotlib

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6])
plt.show()
```

---

## 4. requests

```python
import requests
res = requests.get("https://api.github.com")
print(res.status_code)
```

---

## 5. flask

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"
```

---

## 6. scikit-learn

```python
from sklearn.linear_model import LinearRegression
```

---

# 🔹 **name** Special Variable

```python
if __name__ == "__main__":
    print("Run directly")
```

---

# 🔹 Module vs Package

| Feature | Module      | Package       |
| ------- | ----------- | ------------- |
| Type    | Single file | Folder        |
| Example | math        | numpy         |
| Use     | Small code  | Large project |

---

# 🔹 Install Packages

```bash
pip install numpy
pip install pandas
```

---

# 🚀 Summary

* Module = `.py` file
* Package = collection of modules
* Built-in modules come with Python
* External packages installed via `pip`
* Helps in scalable and clean coding=