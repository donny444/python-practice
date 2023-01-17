class Shape2D:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def __str__(self):
        area = self.width*self.length
        return f"The shape total area is " + str(area)
shape1 = Shape2D(11,12)
print(shape1)
class trapezoid(Shape2D):
    def __init__(self, width, length, width_2):
        super().__init__(width, length)
        self.width_2 = width_2