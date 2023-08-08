print("Welcome to age check")
try:
    age = int(input("Enter your age : "))
except:
    print("Invalid input") #Can't convert to integer
if age < 2:
    print("You are infant")
elif 2 <= age <= 12:
    print("You are child")
elif 13 <= age <= 25:
    print("You are teenager")
elif 26 <= age <= 35:
    print("You are young adult")
elif 36 <= age <= 45:
    print("You are adult")
elif 46 <= age <= 55:
    print("You are golden age")
elif 56 <= age <= 80:
    print("You are elder")
else:
    print("Can't defined")