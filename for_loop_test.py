i = 0
limit = 11
for i in range(10):
    i += 1
    if i%2 != 0:
        print(str(i) + " is Odd Number")
    elif i%2 == 0:
        print(str(i) + " is Even Number")
    else:
        break
print("Finished")