movie=int(input("Enter movie expense :"))
cloths=int(input("Enter cloths expense :"))
family=int(input("Enter family expense :"))

expense=movie+cloths+family

income=int(input("Enter your income :"))

budget=income-expense

print("---------------Total income------------------")
print(income)
print("----------------Total expense-----------------")
print(expense)
print("-----------------Remaining budget---------------")
print(budget)