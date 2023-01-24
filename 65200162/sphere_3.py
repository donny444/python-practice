#parameter/return
r = float(input())
def sphere(r, pi=3.14):
    return (4/3)*pi*(r*r*r)
Volume = sphere(r)
print(Volume)