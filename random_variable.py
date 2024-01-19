import random

result = []
x = 0
for i in range(3):
    toss = random.randint(0, 1)
    result.append(toss)

for i in range(len(result)):
    if(result[i] == 1):
        x += 1

print(result)
print(x)