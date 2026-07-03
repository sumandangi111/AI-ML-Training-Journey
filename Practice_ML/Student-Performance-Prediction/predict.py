import pandas as pd
import joblib
loaded_model=joblib.load("student_model.pkl")
H_s=int(input("enter hours_studied:"))
Atted=int(input("enter attendance:"))
Assign=int(input("enter assignment:"))
previ_mark=int(input("enter previ_marks:"))
new_student=pd.DataFrame({
    "Hours_Studied":[H_s],
    "Attendance":[Atted],
    "Assignments":[Assign],
    "Previous_Marks":[previ_mark]
})
prediction=loaded_model.predict(new_student)
if prediction[0]==1:
    print("Pass")
else:
    print("Fail")