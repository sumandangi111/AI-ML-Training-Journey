import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# load data set
data=pd.read_csv("Decision_Tree_Algo_practical/Cricket_Prediction_model/dataset.csv")
# Encode text data
encoder=LabelEncoder()
data['Weather']=encoder.fit_transform(data['Weather'])
data['Humidity']=encoder.fit_transform(data['Humidity'])
data['Wind']=encoder.fit_transform(data['Wind'])
data['Play']=encoder.fit_transform(data['Play'])

# features and label
x=data[["Weather","Humidity","Wind"]]
y=data["Play"]

# Create model
model=DecisionTreeClassifier()

# Train model
model.fit(x,y)

# make prediction
prediction=model.predict([[0,1,1]])
print("Predict Result: ")
if prediction[0]==1:
    print("Play Cricket")
else:
    print("Do not play Cricket")
