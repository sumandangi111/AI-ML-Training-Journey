import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Attendance": [60,65,70,75,80,85,90,95],
    "Pass": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]

y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Actual:", y_test.values)
# accuracy = accuracy_score(
#     y_test,
#     predictions
# )
# print("Accuracy:", accuracy)

cm = confusion_matrix(
    y_test,
    predictions
)

print(cm)
