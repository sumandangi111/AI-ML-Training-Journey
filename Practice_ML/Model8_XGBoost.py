import pandas as pd

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "Hours_Studied":[1,2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95,100],
    "Pass":[0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

# Features
X = df[["Hours_Studied","Attendance"]]

# Target
y = df["Pass"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Model
# model = XGBClassifier(
#     random_state=42,
#     eval_metric="logloss"
# )

model = XGBClassifier(
    n_estimators=10,
    max_depth=2,
    learning_rate=0.1,
    random_state=42,
    eval_metric="logloss"
)

# Training
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test.values)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)