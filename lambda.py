def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

#print(f(4357))

#Source : https://docs.python.org/3.10/tutorial/controlflow.html#lambda-expressions