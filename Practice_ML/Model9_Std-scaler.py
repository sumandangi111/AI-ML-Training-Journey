import pandas as pd

from sklearn.preprocessing import StandardScaler

data = {
    "Hours_Studied":[2,4,6,8],
    "Salary":[20000,40000,60000,80000]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

print("Scaled Data")
print(scaled_data)
