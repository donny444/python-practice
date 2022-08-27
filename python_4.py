is_male = False
is_female = False
if is_male and not(is_female):
    print("You are a male")
elif is_female and not(is_male):
    print("You are a female")
elif is_male and is_female:
    print("You are male and female?")
else:
    print("You are neither male nor female")