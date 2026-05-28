import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data=pd.read_csv("Decision_Tree_Algo_practical/Loan_Approval_Project/train.csv")

# Check missing values
# print("\nMissing Values:\n")
# print(data.isnull().sum())

# Handle missing Categorical values
data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
data['Married'] = data['Married'].fillna(data['Married'].mode()[0])
data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])
data['Self_Employed'] = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])

# Fill missing numerical values
data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mean())
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mean())


# Drop Loan ID column
data.drop('Loan_ID',axis=1,inplace=True)

# Encode categorical data
encoder=LabelEncoder()
columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]
for col in columns:
    data[col]=encoder.fit_transform(data[col])

# Feature and Label
X=data.drop('Loan_Status',axis=1)
Y=data['Loan_Status']

# Train test split
xtrain,xtest,ytrain,ytest=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Create model
model=DecisionTreeClassifier()

# Train model
model.fit(xtrain,ytrain)

# Make predictions
predict=model.predict(xtest)

# check accuracy
accuracy=accuracy_score(ytest,predict)
print("\nModel Accuracy: ")
print(round(accuracy*100,2),"%")

# New customer data
new_customer = pd.DataFrame([{

    'Gender': 1,
    'Married': 1,
    'Dependents': 0,
    'Education': 0,
    'Self_Employed': 0,
    'ApplicantIncome': 5000,
    'CoapplicantIncome': 2000,
    'LoanAmount': 150,
    'Loan_Amount_Term': 360,
    'Credit_History': 1,
    'Property_Area': 2

}])

# Predict result
prediction = model.predict(new_customer)
print("\nPrediction Result:")

if prediction[0] == 1:
    print("Loan Approved ✅\n")
else:
    print("Loan Rejected ❌\n")
