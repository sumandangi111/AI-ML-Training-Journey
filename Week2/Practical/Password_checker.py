print("-----Password checker-----")
password=input("Enter Password : ")
upper=False
lower=False
digit=False
special_chr=False

Special_char="!@#$%^&*()"

for char in password:
    if char.isupper():
        upper=True
    elif char.islower():
        lower=True
    elif char.isdigit():
        digit=True
    elif char in Special_char:
        special_chr=True

if len(password)>=8 and upper and lower and digit and special_chr :
    print("Strong Password")
else:
    print("Weak Password")
    if len(password) < 8:
        print("Password must be at least 8 characters")
    if not upper:
        print("Password must contain at least one uppercase letter")
    if not lower:
        print("Password must contain at least one lowercase letter")
    if not digit:
        print("Password must contain at least one digit")
    if not special_chr:
        print("Password must contain at least one special character (!@#$%^&*())")