import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data={
    "Hours_studied":[1,2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95,100],
    "Pass":[0,0,0,1,1,1,1,1,1]
}

df=pd.DataFrame(data)
print(df)

X=df[["Hours_studied","Attendance"]]
Y=df["Pass"]

X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.25,
    random_state=42
)

model=DecisionTreeClassifier(
    random_state=42
)
model.fit(X_train,Y_train)
print("Model training complete")

prediction=model.predict(X_test)
print(prediction)
print("Actual:",Y_test.values)

accuracy=accuracy_score(Y_test,prediction)
print("Accuracy:",accuracy)
print("feature importance:",model.feature_importances_)