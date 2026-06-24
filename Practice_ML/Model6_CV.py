import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

data = {
    "Hours_studied":[1,2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95,100],
    "Pass":[0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours_studied","Attendance"]]

y = df["Pass"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=3
)

print("Scores:", scores)

print("Average Score:", scores.mean())