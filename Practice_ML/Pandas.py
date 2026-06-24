# ----------------------------------------------- EDA -------------------------------------

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [22, 25, 28],
    "Salary": [25000, 35000, 50000]
}

df = pd.DataFrame(data)

print(df)
print(type(df))
print(type(df["Age"]))
print(type(df[["Age"]]))

print(df.head())
print("----------------------------------------")
print(df.info())
print("----------------------------------------")
print(df.describe())



# ------------------------------------------------------------ Filtering Data ------------------------------------

data = {
    "Name": ["A", "B", "C"],
    "Age": [22, 25, 28],
    "Salary": [25000, 35000, 50000]
}
df = pd.DataFrame(data)
print(df["Age"] > 24)
print(df[df["Age"] > 24])
print(df[df["Salary"] >= 35000])

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [22, 25, 28, 35],
    "Salary": [25000, 35000, 50000, 70000]
}

df = pd.DataFrame(data)
print(df[df["Salary"] > 40000])
print(df[(df["Age"] > 24) & (df["Salary"] > 40000)])
print(df[(df["Age"] < 30) | (df["Salary"] > 60000)])

# ----------------------------------------- Missing Values --------------------------------------------------
import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [22, 25, np.nan, 35],
    "Salary": [25000, np.nan, 50000, 70000],
    "Department": ["HR", "IT", "IT", "Finance"]
}
df = pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum())

print(df.dropna())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)
print(df["Department"])
print(df["Department"].value_counts())
print(
    df.groupby("Department")["Salary"].mean()
)

# ------------------------- Feature Engineering ----------------------
import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {
    "Department": ["HR", "IT", "IT", "Finance"]
}

df = pd.DataFrame(data)
le = LabelEncoder()

df["Department_Encoded"] = le.fit_transform(
    df["Department"]
)
print(df)