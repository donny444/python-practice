print("-------Health Calculation-------")
w = float(input("Enter your weight [kg] : "))
h = float(input("Enter your height [cm] : "))
age = int(input("Enter your age : "))
sex = str(input("Enter your sex [Male/Female]: "))
if sex == "Male":
    bmr_var = 66+(13.7*w)+(5*h)-(6.8*age)
elif sex == "Female":
    bmr_var = 665+(9.6*w)+(1.8*h)+(4.7*age)
workout = str(input("How frequently do you workout? :\na)rarely or never\nb)1-3 times per week\nc)4-5 times per week\nd)6-7 times per week\ne)up to 2 times per day\n"))
def bmi():
    print("BMI Calculating...")
    bmi_var = w/((h*h)*(0.01*0.01))
    print("Your BMI is : " + str(bmi_var))
def bmr():
    print("BMR Calculating...")
    print("Your BMR is : " + str(bmr_var))
def tdee(x):
    print("TDEE Calculating...")
    if workout == "a":
        tdee_var = 1.2*x
        print("Your TDEE is " + str(tdee_var))
    elif workout == "b":
        tdee_var = 1.375*x
        print("Your TDEE is " + str(tdee_var))
    elif workout == "c":
        tdee_var = 1.55*x
        print("Your TDEE is " + str(tdee_var))
    elif workout == "d":
        tdee_var = 1.7*x
        print("Your TDEE is " + str(tdee_var))
    elif workout == "e":
        tdee_var = 1.9*x
        print("Your TDEE is " + str(tdee_var))
bmi()
bmr()
tdee(bmr_var)