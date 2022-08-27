numbers_list = [
    [1, 2, 3,],
    [4, 5, 6,],
    [7, 8, 9,],
    [10]
]
try:
    yn = str(input("Print 1-10? [Y/N] : "))
except:
    print("Invalid value")
if yn == "Y":
    for row in numbers_list:
        for col in row:
            print(col)
elif yn == "N":
    print("Not printing 1-10")
else:
    print("Can't defined")