import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Hours_Studied": [2,3,6,8],
    "Attendance": [60,65,85,95],
    "Pass": [0,0,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Pass"]

model = DecisionTreeClassifier()
model.fit(X, y)
print("Training Complete")