class Shape:
    pass

class Shape2D(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def getArea(self):
        self.area = self.width*self.length
        print(f"Shape Area: {self.area}")

    #def display(self):
    #    print(f"Shape width: {self.width}")
    #    print(f"Shape length: {self.length}")
    #    print(f"Shape Area: {self.area}")
    
    def __del__(self):
        pass

class Circle(Shape2D):
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        self.area = self.pi*(self.radius**2)
        print(f"Circle Area: {self.area}")
    
    def __del__(self):
        pass

class Trapezoid(Shape2D):
    def __init__(self, width, length, length_1, length_2):
        Shape2D.__init__(self, width, length)
        self.length_1 = length_1
        self.length_2 = length_2
    
    def getArea(self):
        self.area = 1/2*(self.length_1+self.length_2)*self.width
        print(f"Trapezoid Area: {self.area}")

    def __del__(self):
        pass

obj1 = Shape2D(9, 25)
obj1.getArea()

obj2 = Circle(33)
obj2.getArea()

obj3 = Trapezoid(3, None, 4, 2)
obj3.getArea()