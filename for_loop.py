words = ["Donny", "yed", "hee", "Cake"]
x = 1
t = 0
for word in words:
    print("Step_" + str(x) + ": " + word)
    x += 1
while t != 13:
    t += 1
    print(str(t) + "T")
    if t == 9:
        t += 1