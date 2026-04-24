import random
secret_number=random.randint(1,100)
print("-----Number Guessing Game-----")
print("Enter number between 1 to 100")
while True:
    guess=int(input("Enter your guess :"))
    if guess<secret_number:
        print("no. is low")
    elif guess>secret_number:
        print("no. is high")
    else:
        print("Correct guess")
        break