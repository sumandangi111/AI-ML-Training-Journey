balance = 1000
def check_balance():
    print(f"Current Balance: ₹{balance}")

def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        print("Amount Deposited Successfully")
        print("Updated Balance:", balance)

    else:
        print("Invalid Amount")

def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid Amount")

    elif amount > balance:
        print("Insufficient Balance")

    else:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)


while True:

    print("\n===== MINI ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank You for Using ATM")
        break

    else:
        print("Invalid Choice")