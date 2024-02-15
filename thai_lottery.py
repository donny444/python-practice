import random

win1st = ""
win3head = []
win3tail = []
win2tail = ""

for i in range(6):
    digit = str(random.randint(0, 9))
    win1st += digit

for i in range(2):
    digits = ""
    for j in range(3):
        digit = str(random.randint(0, 9))
        digits += digit
    win3head.append(digits)

for i in range(2):
    digits = ""
    for j in range(3):
        digit = str(random.randint(0, 9))
        digits += digit
    win3tail.append(digits)

for i in range(2):
    digit = str(random.randint(0, 9))
    win2tail += digit

print("รางวัลที่1: " + win1st)
print("รางวัลเลขหน้า3ตัว: ", end="")
print(win3head)
print("รางวัลเลขท้าย3ตัว: ", end="")
print(win3tail)
print("รางวัลเลขท้าย2ตัว: " + win2tail)

prize = 0
lottery = input("Enter your lottery digits: ")

try:
    if(lottery == ""):
        raise ValueError("Please enter the lottery digits")
    if(len(lottery) != 6):
        raise ValueError("Lottery must have 6 digits")
    for i in range(6):
        if(((lottery[i] != 0) or (lottery[i] != 1) or (lottery[i] != 2) or (lottery[i] != 3) or (lottery[i] != 4) or (lottery[i] != 5) or (lottery[i] != 6) or (lottery[i] != 7) or (lottery[i] != 8) or (lottery[i] != 9))):
            raise ValueError("Lottery must contains only number")
except ValueError as e:
    print(e)

for i in range(6):
    if(lottery[i] == win1st[i]):
        win = True
    else:
        prize = 0
        win = False
        break
if(win == True):
    print("You won the 1st prize")
    prize += 6000000
    print("Prize: " + str(prize))

for i in range(2):
    for j in range(3):
        if(lottery[j] == win3head[i][j]):
            win = True
        else:
            win = False
            break
    if(win == True):
        print("You won a 3 head digits prize")
        prize += 4000
        print("Prize: " + str(prize))

for i in range(2):
    for j in range(3, 6):
        if(lottery[j] == win3tail[i][j-3]):
            win = True
        else:
            win = False
            break
    if(win == True):
        print("You won a 3 tail digits prize")
        prize += 4000
        print("Prize: " + str(prize))

for i in range(2):
    if(lottery[i+4] == win2tail[i]):
        win = True
    else:
        win = False
        break
if(win == True):
    print("You won the 2 tail digits prize")
    prize += 2000
    print("Prize: " + str(prize))