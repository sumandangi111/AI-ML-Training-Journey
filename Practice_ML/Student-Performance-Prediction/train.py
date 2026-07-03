import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv("Practice_ML\Student-Performance-Prediction\data\students.csv")
print(df.head())
print(df.info())
print(df.describe())

X=df[[
    "Hours_Studied","Attendance","Assignments","Previous_Marks"
]]
Y=df["Pass"]

X_train, X_test, Y_train, Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
model=RandomForestClassifier(
    random_state=42
)
model.fit(X_train,Y_train)
predictions=model.predict(X_test)
accuracy=accuracy_score(Y_test,predictions)
print("Accuracy",accuracy)

joblib.dump(
    model,
    "student_model.pkl"
)
print("Model Saved Successfully!")