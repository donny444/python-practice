# Protected Modifier (_)
class videogame1:
    # Protected attribute
    def __init__(self, name, category, price):
        self._name = name
        self._category = category
        self._price = price
        self._display()

    # Protected method
    def _display(self):
        print("Name: {}".format(self._name))
        print("Category: {}".format(self._category))
        print("Price: {}".format(self._price))
        
    def __del__(self):
        print("Destructure")

class videogame2(videogame1):
    def __init__(self, name, category, price, platform):
        self._platform = platform
        videogame1.__init__(self, name, category, price)
        videogame1._display(self)
        print("Platform: {}".format(self._platform))

vg1 = videogame1("Elden Ring", "Soul-Like RPG", 69.99)
print("\n")
vg2 = videogame2("GTA V", "Open World", 59.99, "PC")