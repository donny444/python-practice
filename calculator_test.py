print("------Calculator Test------")
try:
    x = float(input("Enter value of X : "))
    y = float(input("Enter value of Y : "))
    op = str(input("Enter operator : "))
except:
    print("Invalid value")
if op == "+":
    print("The result is",x + y)
elif op == "-":
    print("The result is",x - y)
elif op == "*":
    print("The result is",x*y)
elif op == "/":
    print("The result is",x/y)
else:
    print("Unknown")