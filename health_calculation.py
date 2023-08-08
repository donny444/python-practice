print("-------Health Calculation-------")
w = float(input("Enter your weight [kg] : "))
h = float(input("Enter your height [cm] : "))
age = int(input("Enter your age : "))
sex = str(input("Enter your sex [Male/Female]: "))
workout = str(input("How frequently do you workout? :\na)rarely or never\nb)1-3 times per week\nc)4-5 times per week\nd)6-7 times per week\ne)up to 2 times per day\n"))
def bmi(w, h):
    print("BMI Calculating...")
    bmiVal = float(w/((h*h)*(0.01*0.01)))
    return "Your BMI is : " + str(bmiVal)
def bmr(w, h, sex, age):
    global bmrVal;
    print("BMR Calculating...")
    if sex == "Male":
        bmrVal = float(66+(13.7*w)+(5*h)-(6.8*age))
    elif sex == "Female":
        bmrVal = float(665+(9.6*w)+(1.8*h)-(4.7*age))
    return "Your BMR is : " + str(bmrVal)
def tdee(bmrVal):
    print("TDEE Calculating...")
    if workout == "a":
        tdeeVal = 1.2*bmrVal
        return "Your TDEE is " + str(tdeeVal)
    elif workout == "b":
        tdeeVal = 1.375*bmrVal
        return "Your TDEE is " + str(tdeeVal)
    elif workout == "c":
        tdeeVal = 1.55*bmrVal
        return "Your TDEE is " + str(tdeeVal)
    elif workout == "d":
        tdeeVal = 1.7*bmrVal
        return "Your TDEE is " + str(tdeeVal)
    elif workout == "e":
        tdeeVal = 1.9*bmrVal
        return "Your TDEE is " + str(tdeeVal)
print(bmi(w, h))
print(bmr(w, h, sex, age))
print(tdee(bmrVal))

#Next time: use try except