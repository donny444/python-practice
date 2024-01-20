import random

coin = ("H", "T")
result = []
#result = ""
x = 0

for i in range(8):
    #toss = random.randint(0, 1)
    toss = random.choice(coin)
    result.append(toss)

for i in range(len(result)):
    if(result[i] == "H"):
        x += 1

print(result)
print(x)