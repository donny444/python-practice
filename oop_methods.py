from datetime import date

class Dessert:
    def __init__(self, name):
        self.name = name

    #classmethod
    def display(self):
        return "The Dessert is: " + self.name
    
class Health:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    #classmethod
    def classBmi(self):
        return self.weight / ((self.height**2)/10000)
    
    @staticmethod
    def staticBmi(weight, height):
        return weight / ((height**2)/10000)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def isAdult(age):
        return age > 18

dessert1 = Dessert("Chocolate")
dessert2 = Dessert("Lollipop")
dessert3 = Dessert("Rotee")

health1 = Health(80, 180)

print(dessert1.display())
print(health1.classBmi())
print(health1.staticBmi(80, 180))

person1 = Person("Donny", 19)
person2 = Person("Donny", 2004)

print(person1.age)
print(person2.age)

print(f"Donny is an adult?: {Person.isAdult(19)}")