i = 0
n = int(input("Enter Natural Number: "))
if n>0:
    for i in range(n):
        i += 1
        if i%2 != 0:
            print(str(i) + " is Odd Number")
        elif i%2 == 0:
            print(str(i) + " is Even Number")
        else:
            break
else:
    print("Only Natural Number")
print("Finished")