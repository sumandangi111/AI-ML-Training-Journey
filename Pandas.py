# ----------------------------------------------- EDA -------------------------------------

import pandas as pd
'''
data = {
    "Name": ["A", "B", "C"],
    "Age": [22, 25, 28],
    "Salary": [25000, 35000, 50000]
}

df = pd.DataFrame(data)

# print(df)
# print(type(df))
# print(type(df["Age"]))
# print(type(df[["Age"]]))

print(df.head())
print("----------------------------------------")
print(df.info())
print("----------------------------------------")
print(df.describe())'''



# ------------------------------------------------------------ Filtering Data ------------------------------------

'''data = {
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
print(df[(df["Age"] < 30) | (df["Salary"] > 60000)])'''

# -------------------------------------------------------------------------------------------

df=pd.read_csv("employees.csv")
print(df)