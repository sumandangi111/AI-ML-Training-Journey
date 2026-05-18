# 1. Introduction to Artificial Intelligence (AI)

Artificial Intelligence (AI) means creating machines or software that can perform tasks which normally require human intelligence.

Examples:
- Understanding language
- Recognizing images
- Making decisions
- Learning from data
- Predicting results

## Goal of AI
Provide intelligence to machines so they can:
- Learn
- Think
- Analyze
- Predict
- Improve automatically

---

# 2. Machine Learning Foundations

Machine Learning (ML) is a subset of AI.

In ML, machines learn patterns from data instead of being explicitly programmed.

## Basic Flow of Machine Learning

```text
Data Collection → Data Processing → Model Training → Prediction
```

---

# 3. Types of Machine Learning

## Supervised Learning
The model learns using labeled data.

### Example
Input: House features  
Output: House price

### Common Algorithms
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest
- SVM

---

## Unsupervised Learning
The model learns from unlabeled data.

### Common Algorithms
- K-Means Clustering
- PCA
- DBSCAN

---

## Reinforcement Learning
The model learns by rewards and punishments.

### Applications
- Robotics
- Game AI
- Self-driving cars

---

# 4. Model Building

## Steps
1. Collect data
2. Clean data
3. Train model
4. Test model
5. Deploy model

---

# 5. Fine-Tuning

Fine-tuning means training an existing pre-trained model on custom data.

```text
Existing Model + Custom Data → Fine-Tuned Model
```

### Advantages
- Saves time
- Saves cost
- Better performance on custom tasks

---

# 6. RAG (Retrieval-Augmented Generation)

RAG combines retrieval systems with language models.

```text
User Question → Search Documents → Retrieve Data → Generate Answer
```

### Uses
- AI Chatbots
- PDF Chat systems
- Company assistants

---

# 7. Important Libraries

## Scikit-Learn
Used for traditional machine learning.

## Transformers
Used for NLP and LLMs.

## TensorFlow
Google’s deep learning framework.

## PyTorch
Popular deep learning framework.

---

# 8. Data Collection

## Sources
- Kaggle
- Hugging Face
- APIs
- CSV files
- Databases

---

# 9. Kaggle

Kaggle is used for:
- Datasets
- Competitions
- ML practice
- Real-world projects

---

# 10. Hugging Face

Hugging Face provides:
- Pretrained models
- Datasets
- APIs
- AI deployment tools

---

# 11. Data Visualization

## Libraries
- Matplotlib
- Seaborn
- Plotly

---

# 12. AI/ML Workflow

```text
Problem Statement
       ↓
Data Collection
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Evaluation
       ↓
Deployment
```

---

# 13. Deep Learning Basics

Deep Learning uses neural networks.

## Applications
- Computer Vision
- NLP
- Speech Recognition

---

# 14. Transformers

Transformers are used in:
- ChatGPT
- Gemini
- Claude
- Llama

### Advantages
- Better context understanding
- Parallel processing
- Scalable training

---

# 15. Important Terms

## Dataset
Collection of data.

## Features
Input variables.

## Labels
Expected outputs.

## Overfitting
Model memorizes training data.

## Underfitting
Model fails to learn patterns.

---

# 16. AI Frameworks

## Traditional ML
- Scikit-Learn
- XGBoost

## Deep Learning
- TensorFlow
- PyTorch

## LLM Development
- LangChain
- Transformers
- LlamaIndex

---

# 17. LangChain

LangChain helps build LLM applications.

### Features
- Prompt chaining
- Memory
- Tool calling
- RAG pipelines

---

# 18. APIs in AI

Popular APIs:
- OpenAI API
- Gemini API
- Hugging Face API

---

# 19. Deployment

## Tools
- Docker
- FastAPI
- Render
- Railway
- AWS

---

# 20. Skills Required

## Programming
- Python
- SQL
- Git

## Mathematics
- Statistics
- Probability
- Linear Algebra

---

---

# 21. Quick Revision

```text
AI → Intelligence in machines
ML → Learning from data
DL → Neural networks
RAG → Retrieval + Generation
Fine-Tuning → Training existing models
Transformers → Modern LLM architecture
```
# -------------------------------------------------------

# NumPy, Pandas, and Matplotlib Notes

# 1. NumPy

## What is NumPy?

NumPy (Numerical Python) is a Python library used for:
- Numerical operations
- Array handling
- Mathematical calculations
- Scientific computing

It is faster than Python lists because arrays are optimized for performance.

---

# Installing NumPy

```bash
pip install numpy
```

---

# Importing NumPy

```python
import numpy as np
```

---

# Creating Arrays

## 1D Array

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
```

Output:
```python
[1 2 3 4]
```

---

## 2D Array

```python
arr = np.array([[1, 2], [3, 4]])
print(arr)
```

Output:
```python
[[1 2]
 [3 4]]
```

---

# Important NumPy Functions

## zeros()

Creates an array filled with zeros.

```python
np.zeros((2, 3))
```

---

## ones()

Creates an array filled with ones.

```python
np.ones((2, 2))
```

---

## arange()

Creates values within a range.

```python
np.arange(1, 10)
```

---

## linspace()

Creates evenly spaced numbers.

```python
np.linspace(0, 1, 5)
```

---

# Array Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
```

Output:
```python
[5 7 9]
[4 10 18]
```

---

# Shape and Size

```python
arr.shape
arr.size
arr.ndim
```

- shape → dimensions
- size → total elements
- ndim → number of dimensions

---

# Reshaping Arrays

```python
arr = np.array([1,2,3,4,5,6])

new_arr = arr.reshape(2,3)
print(new_arr)
```

---

# Advantages of NumPy

- Faster computation
- Memory efficient
- Supports multi-dimensional arrays
- Used in ML and Data Science

---

# 2. Pandas

## What is Pandas?

Pandas is a Python library used for:
- Data analysis
- Data cleaning
- Data manipulation
- Reading and writing files

---

# Installing Pandas

```bash
pip install pandas
```

---

# Importing Pandas

```python
import pandas as pd
```

---

# Series in Pandas

A Series is a one-dimensional labeled array.

```python
s = pd.Series([10, 20, 30])
print(s)
```

---

# DataFrame in Pandas

A DataFrame is a table-like structure.

```python
data = {
    "Name": ["Aman", "Rahul"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)
print(df)
```

---

# Reading CSV Files

```python
df = pd.read_csv("data.csv")
```

---

# Viewing Data

## head()

Shows first 5 rows.

```python
df.head()
```

---

## tail()

Shows last 5 rows.

```python
df.tail()
```

---

## info()

Displays dataset information.

```python
df.info()
```

---

## describe()

Shows statistical summary.

```python
df.describe()
```

---

# Selecting Columns

```python
df["Name"]
```

---

# Selecting Multiple Columns

```python
df[["Name", "Age"]]
```

---

# Filtering Data

```python
df[df["Age"] > 21]
```

---

# Handling Missing Values

## Check missing values

```python
df.isnull()
```

---

## Remove missing values

```python
df.dropna()
```

---

## Fill missing values

```python
df.fillna(0)
```

---

# Saving Data

```python
df.to_csv("output.csv")
```

---

# Advantages of Pandas

- Easy data handling
- Works with large datasets
- Powerful analysis tools
- Widely used in ML projects

---

# 3. Matplotlib

## What is Matplotlib?

Matplotlib is a Python library used for:
- Data visualization
- Creating graphs and charts
- Plotting data

---

# Installing Matplotlib

```bash
pip install matplotlib
```

---

# Importing Matplotlib

```python
import matplotlib.pyplot as plt
```

---

# Line Plot

```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()
```

---

# Bar Chart

```python
subjects = ["Math", "Science", "English"]
marks = [80, 90, 75]

plt.bar(subjects, marks)
plt.show()
```

---

# Pie Chart

```python
sizes = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels)
plt.show()
```

---

# Scatter Plot

```python
x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

plt.scatter(x, y)
plt.show()
```

---

# Adding Labels and Title

```python
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Graph")
```

---

# Grid in Plot

```python
plt.grid()
```

---

# Advantages of Matplotlib

- Easy visualization
- Supports multiple chart types
- Helpful for analysis
- Used in Data Science and ML

---

# Difference Between NumPy, Pandas, and Matplotlib

| Library | Purpose |
|---|---|
| NumPy | Numerical operations and arrays |
| Pandas | Data analysis and manipulation |
| Matplotlib | Data visualization and plotting |

---

# Real-World Workflow

```text
Collect Data
      ↓
Use Pandas for Cleaning
      ↓
Use NumPy for Calculations
      ↓
Use Matplotlib for Visualization
```

---

# Summary

## NumPy
- Used for numerical computing
- Works with arrays
- Fast and efficient

## Pandas
- Used for data analysis
- Handles tables and datasets
- Supports CSV and Excel files

## Matplotlib
- Used for plotting graphs
- Creates visual representations of data

