import random

coin = ("H", "T")
n_e = 0
n_s = 3
result = ""

for i in range(n_s):
    toss = random.choice(coin)
    result = result + toss
    if(toss == "T"):
        n_e = n_e + 1
p_e = n_e / n_s

print(result)
print(n_e)
print(p_e)