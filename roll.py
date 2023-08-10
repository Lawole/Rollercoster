#  ALL DIE NA DIE ROLLACOASTER
print("Welcome to ALL DIE NA DIE Rollercoaster")
height = int(input("What is your height in cm?\n "))
bill = 0

if height >= 120:
    print("Welcome! you can ride")
    age = int(input("How old are you?  "))
    if age > 45:
        print("You are almost dead, just ride for free")
    elif age >= 18 and age <= 45:
        bill = 500
        print(f"Adults tickets are ${bill} to ride")
    elif age > 12 and age <= 18:
        bill = 400
        print(f"Youths tickets are ${bill} to ride")
    else:
        bill = 200
        print(f"Children tickets are ${bill} to ride")

    pictures = input("Do you want an extra photo? costs extra $70  type y for yes or n for no.  ")
    if pictures == "Y":
        bill += 70

    print(f"Your final bill is ${bill}")
else:
    print("Please eat more protein so you can grow taller")
