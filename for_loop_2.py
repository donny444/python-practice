print("-----Multiply Program-----")
try:
    n1=int(input("Enter positive interger: "))
    if n1>0:
        for n2 in range(1,13):
            print(str(n1) + "x" + str(n2) + "=" + str(n1*n2))
    elif n1<0:
        print("It's negative interger!")
    elif n1==0:
        print("It's zero interger")
except:
    print("It's not interger")