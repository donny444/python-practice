class outfit:
    def __init__(self, type, brand, price_THB):
        self.type = type
        self.brand = brand
        self.price_THB = price_THB
        self.display()
        self.__str__()
    def display(self):
        print("Type: {}".format(self.type))
        print("Brand: {}".format(self.brand))
        print("THB Price: {}".format(self.price_THB))
    def __str__(self):
        return f"Finished from the mother class"

obj1 = outfit("Sneaker", "Adidas", 3500)
print(obj1)