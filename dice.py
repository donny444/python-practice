import random

result = []
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range(50000000):
    roll = random.randint(1, 6)
    result.append(roll)

for i in range(len(result)):
    if(result[i] == 1):
        one += 1
    if(result[i] == 2):
        two += 1
    if(result[i] == 3):
        three += 1
    if(result[i] == 4):
        four += 1
    if(result[i] == 5):
        five += 1
    if(result[i] == 6):
        six += 1

f_1 = one / len(result)
f_2 = two / len(result)
f_3 = three / len(result)
f_4 = four / len(result)
f_5 = five / len(result)
f_6 = six / len(result)

e_x = 1*f_1 + 2*f_2 + 3*f_3 + 4*f_4 + 5*f_5 + 6*f_6

print(e_x)