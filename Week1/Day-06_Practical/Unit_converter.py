print("Select conversion type")
print("1. Length Conversion")
print("2. Weight Conversion")
print("3. Temperature Conversion")

choice=int(input("Enter Choice (1-3) :"))
if choice==1:
    print("Length Conversion :")
    print("1. KM to Meter")
    print("2. Meter to KM")
    print("3. Meter to CM")
    print("4. CM to Meter")
    print("5. MM to CM")
    print("6. CM to MM")
    
    option=int(input ("enter option :"))
    if option==1:
        km=float(input("Enter KM: "))
        print("Meter :",km*1000)
    elif option==2:
        meter=float(input("Enter meter: "))
        print("Kilo Meter :",meter/1000)
    elif option==3:
        meter=float(input("Enter meter: "))
        print("CM :",meter*100)
    elif option==4:
        Cm=float(input("Enter CM: "))
        print("Meter :",Cm/100)
    elif option==5:
        mm=float(input("Enter mm: "))
        print("CM :",mm/10)
    elif option==6:
        Cm=float(input("Enter CM: "))
        print("Meter :",Cm*10)
    else:
        print("Invalid Operator")

elif choice==2:
    print("Weight Conversion: ")
    print("1. KG to Gram")
    print("2. Gram to KG")

    option = int(input("Enter option: "))

    if option == 1:
        kg = float(input("Enter KG: "))
        print("Grams:", kg * 1000)

    elif option == 2:
        g = float(input("Enter Grams: "))
        print("KG:", g / 1000)

    else:
        print("Invalid option")

elif choice==3:
    print("Temperature Conversion:")
    print("1. Celsius to Kelvin")
    print("2. Kelvin to Celsius")

    option = int(input("Enter option: "))

    if option == 1:
        c = float(input("Enter Celsius: "))
        print("Kelvin:", c + 273.15)

    elif option == 2:
        k = float(input("Enter Kelvin: "))
        print("Celsius:", k - 273.15)

    else:
        print("Invalid option")

else:
    print("Invalid choice")