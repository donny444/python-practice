# Private Modifier (__)
class videogame1:
    # Private attribute
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price

    # Private method
    def __display(self):
        print("Name: {}".format(self.__name))
        print("Category: {}".format(self.__category))
        print("Price: {}".format(self.__price))
        
    def __del__(self):
        print("Destructure")

class videogame2(videogame1):
    def __init__(self, name, category, price, platform):
        self.__platform = platform
        videogame1.__init__(self, name, category, price)

    def __display(self):
        videogame1.__display(self)
        print("Platform: {}".format(self.__platform))

vg1 = videogame2("Elden Ring", "Soul-Like RPG", 69.99, "PS5")
vg1.__display()