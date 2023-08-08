from fashion import outfit

class top(outfit):
    def __init__(self, type, brand, price_THB, color, size):
        outfit.type = type
        outfit.brand = brand
        outfit.price_THB = price_THB
        self.color = color
        self.size = size
        outfit.display(self)
        #outfit.__init__(self, type, brand, price_THB)
        self.display()
    def display(self):
        print("color: {}".format(self.color))
        print("Size: {}".format(self.size))

obj3 = top("Hoodie", "Carhartt", 2000, "Orange", "L")