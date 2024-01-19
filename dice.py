import random

result = []
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range(500):
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

print(one/len(result))
print(two/len(result))
print(three/len(result))
print(four/len(result))
print(five/len(result))
print(six/len(result))