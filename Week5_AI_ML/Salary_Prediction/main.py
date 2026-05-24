import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data
data =pd.read_csv("Week5_AI_ML/Salary_Prediction/salary_data.csv")

# Selecting features
x=data[["experience","age"]]

# Selecting target
y=data["salary"]

# Split data
xtrain,xtest,ytrain,ytest=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model=LinearRegression()

# Train model
model.fit(xtrain,ytrain)

# Predict test data
predict=model.predict(xtest)

# Evaluate model
error=mean_squared_error(ytest,predict)
print("MSE: ",error)

# Predict new employee data
new_employee=[[13,45]]

# Predict final salary
predict_salary=model.predict(new_employee)

print("Result :",predict_salary)