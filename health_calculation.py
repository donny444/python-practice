print("-------Health Calculation-------")
w = float(input("Enter your weight [kg] : "))
h = float(input("Enter your height [cm] : "))
age = int(input("Enter your age : "))
sex = str(input("Enter your sex [Male/Female]: "))
workout = str(input("How frequently do you workout? :\na)rarely or never\nb)1-3 times per week\nc)4-5 times per week\nd)6-7 times per week\ne)up to 2 times per day\n"))
def bmi(w, h):
    print("BMI Calculating...")
    return float(w/((h*h)*(0.01*0.01)))
def bmr(w, h, sex, age):
    print("BMR Calculating...")
    if sex == "Male":
        return float(66+(13.7*w)+(5*h)-(6.8*age))
    elif sex == "Female":
        return float(665+(9.6*w)+(1.8*h)-(4.7*age))
def tdee():
    print("TDEE Calculating...")
    if workout == "a":
        return 1.2*bmr(w, h, sex, age)
    elif workout == "b":
        return 1.375*bmr(w, h, sex, age)
    elif workout == "c":
        return 1.55*bmr(w, h, sex, age)
    elif workout == "d":
        return 1.7*bmr(w, h, sex, age)
    elif workout == "e":
        return 1.9*bmr(w, h, sex, age)
print("Your BMI Value is " + str(bmi(w, h)))
print("Your BMR Value is " + str(bmr(w, h, sex, age)))
print("Your TDEE Value is " + str(tdee()))

#Next time: use try except