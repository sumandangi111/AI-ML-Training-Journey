'''import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Marks": [20,30,35,50,55,65,75,85]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
Y = df["Marks"]

model = LinearRegression()
model.fit(X, Y)

print("Training Complete")
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

#prediction = model.predict([[9]])
new_data = pd.DataFrame({
    "Hours_Studied": [9]
})
prediction = model.predict(new_data)
print("Prediction:", prediction)'''

# ----------------------------------------------------------------

'''import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Attendance": [60,65,70,75,80,85,90,95],
    "Marks": [20,30,35,50,55,65,75,85]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)'''

# -------------------------------------------------------

'''import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Attendance": [60,65,70,75,80,85,90,95],
    "Marks": [20,30,35,50,55,65,75,85]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X, y)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)'''

# -------------------------------------------------------

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Attendance": [60,65,70,75,80,85,90,95],
    "Marks": [20,30,35,50,55,65,75,85]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

prediction=model.predict(X_test)
print("predicted value :",prediction)
print("Actual value:",y_test.values)
print("MSE:", mean_squared_error(y_test, prediction))
print("R2 Score:", r2_score(y_test, prediction))