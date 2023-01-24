#parameter/return
def trapezoid(w1, w2, h):
    return (1/2)*(w1+w2)*h
w1 = int(input())
w2 = int(input())
h = int(input())
Area = trapezoid(w1, w2, h)
print(Area)