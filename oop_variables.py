class Rapper:
    career = "rapper" #static or class variable
    def __init__(self, aka, genres):
        self.aka = aka #instance variable
        self.genres = genres #instance variable
    
rapperA = Rapper("Travis Scott", "Trap")
rapperB = Rapper("Eminem", "Lyrical")
rapperC = Rapper("Illslick", "Country")

print(rapperA.career)
print(rapperB.career)
print(rapperC.career)
print(rapperA.aka)
print(rapperB.aka)
print(rapperC.aka)
print(rapperA.genres)
print(rapperB.genres)
print(rapperC.genres)