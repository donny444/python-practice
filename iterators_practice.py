class myNum:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myClass = myNum(2)
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))