#no parameter/return
def trapezoid():
    w1 = int(input())
    w2 = int(input())
    h = int(input())
    return str((1/2)*(w1+w2)*h)
Area = trapezoid()
print(Area)