from fashion import outfit

class top(outfit):
    def __init__(self, type, brand, price_THB, color, size):
        self.color = color
        self.size = size
        super().__init__(type, brand, price_THB)
    def display(self):
        print("color: {}".format(self.color))
        print("Size: {}".format(self.size))

obj3 = top("Hoodie", "Carhartt", 2000, "Orange", "L")