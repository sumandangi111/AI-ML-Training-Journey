import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# data set load
data=pd.read_csv("stud.csv")
x=data[["study_hours","attendance_percentage","sleep_hours"]]
y=data["marks"]
xtrain,xtest,ytrain,ytest=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
# create model
model=LinearRegression()
# train model
model.fit(xtrain,ytrain)
# predict
predict=model.predict(xtest)
# evaluate
error=mean_squared_error(ytest,predict)
# test data
new_student=[[6,88,7.5]]
predict_marks=model.predict(new_student)
print("result :",predict_marks)