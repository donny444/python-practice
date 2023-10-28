#number = [4*1, 4*9, 4*3, 4*7, 4*8, 4*6, 4*2, 4*4, 4*5, 4*0]
number = [53, 52, 51, 50, 49, 48, 47, 46, 982]
def output():
    for i in range(len(number)):
        print(number[i], end=" ")

output()
print("")
for i in range(1, len(number)):
    k = number[i]
    j = i-1
    while j >= 0 and k < number[j]:
        number[j+1] = number[j]
        j -= 1
    number[j+1] = k
output()