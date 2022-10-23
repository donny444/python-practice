print("-------Health Calculation-------")
w = float(input("Enter your weight [kg] : "))
h = float(input("Enter your height [cm] : "))
age = int(input("Enter your age : "))
sex = str(input("Enter your sex [Male/Female]: "))
bmiVal = float()
bmrVal = float()
tdeeVal = float()
if sex == "Male":
    bmrVal = 66+(13.7*w)+(5*h)-(6.8*age)
elif sex == "Female":
    bmrVal = 665+(9.6*w)+(1.8*h)+(4.7*age)
workout = str(input("How frequently do you workout? :\na)rarely or never\nb)1-3 times per week\nc)4-5 times per week\nd)6-7 times per week\ne)up to 2 times per day\n"))
def bmi():
    print("BMI Calculating...")
    bmiVal = w/((h*h)*(0.01*0.01))
    print("Your BMI is : " + str(bmiVal))
def bmr():
    print("BMR Calculating...")
    print("Your BMR is : " + str(bmrVal))
def tdee(bmrVal):
    print("TDEE Calculating...")
    if workout == "a":
        tdeeVal = 1.2*bmrVal
        print("Your TDEE is " + str(tdeeVal))
    elif workout == "b":
        tdeeVal = 1.375*bmrVal
        print("Your TDEE is " + str(tdeeVal))
    elif workout == "c":
        tdeeVal = 1.55*bmrVal
        print("Your TDEE is " + str(tdeeVal))
    elif workout == "d":
        tdeeVal = 1.7*bmrVal
        print("Your TDEE is " + str(tdeeVal))
    elif workout == "e":
        tdeeVal = 1.9*bmrVal
        print("Your TDEE is " + str(tdeeVal))
    return tdeeVal
bmi()
bmr()
tdee(bmrVal)