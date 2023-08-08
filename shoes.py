import fashion

class shoes(fashion.outfit):
    def __init__(self, type, brand, price_THB, section, series, color_1, color_2, size_US, collab):
        fashion.outfit.type = type
        fashion.outfit.brand = brand
        fashion.outfit.price_THB = price_THB
        self.section = section
        self.series = series
        self.color_1 = color_1
        self.color_2 = color_2
        self.size_US = size_US
        self.collab = collab
        fashion.outfit.__init__(self, type, brand, price_THB)
        #self.display()
    def display(self):
        print("Section: {}".format(self.section))
        print("Series: {}".format(self.series))
        print("Primary color: {}".format(self.color_1))
        print("Secondary color: {}".format(self.color_2))
        print("US Size: {}".format(self.size_US))
        print("Collaboration: {}".format(self.collab))

obj2 = shoes("Sneaker", "Nike", 3600, "Basketball", "Air Force 1", "Black", "Yellow", 9.5, None)