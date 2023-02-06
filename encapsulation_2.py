# Private Modifier (__)
class videogame:
    # Private attribute
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price

        self.__display()
    # Private method
    def __display(self):
        print("Name: {}".format(self.__name))
        print("Category: {}".format(self.__category))
        print("Price: {}".format(self.__price))
        
    def __del__(self):
        print("Destructure")

vg1 = videogame("Elden Ring", "Soul-Like RPG", 69.99)
vg1.__display()