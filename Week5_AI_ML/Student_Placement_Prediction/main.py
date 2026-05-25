import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
data=pd.read_csv("Week5_AI_ML/Student_Placement_Prediction/placement_data.csv")
# SElecting features(input)
x=data[["cgpa","communication_skills","projects"]]
# Selecting target(output)
y=data["placed"]

# Split data
xtrain,xtest,ytrain,ytest=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model=LogisticRegression()
# Train model
model.fit(xtrain,ytrain)
# Predict test data
predict=model.predict(xtest)
# Evaluate model
accuracy=accuracy_score(ytest,predict)
print("Accuracy: ",accuracy)

# new student data
new_student=pd.DataFrame({
    "cgpa":[8.2],
    "communication_skills":[8],
    "projects":[4]
})

# Result
result=model.predict(new_student)
if result[0]==1:
    print("Student wiil be Placed")
else:
    print("Student will NOT Be Placed")