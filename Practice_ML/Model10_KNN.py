import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data={
    "Stu_Hours":[2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95],
    "Pass":[0,0,0,1,1,1,1,1]
}

df=pd.DataFrame(data)
X=df[["Stu_Hours","Attendance"]]
Y=df["Pass"]

X_train, X_test, Y_train, Y_test=train_test_split(
    X,
    Y,
    test_size=0.25,
    random_state=42
)

# Scaling
Scaler=StandardScaler()
X_train=Scaler.fit_transform(X_train)
X_test=Scaler.transform(X_test)

# Model
Model=KNeighborsClassifier(n_neighbors=3)
Model.fit(X_train,Y_train)
prediction=Model.predict(X_test)
print("Predictions:",prediction)
print("Actual:",)
print("Accuracy:",accuracy_score(Y_test,prediction))