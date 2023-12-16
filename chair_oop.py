class Furniture:
    def __init__(self, type, material1, material2, price):
        self._type = type
        self._material1 = material1
        self._material2 = material2
        self._priceTHB = price

    def _display(self):
        print(f"type: {self._type}")
        print(f"1st material: {self._material1}")
        print(f"2nd material: {self._material2}")
        print(f"THB Price: {self._priceTHB}")
    
    def __del__(self):
        pass

class Chair(Furniture):
    def __init__(self, type, material1, material2, priceTHB, wheeling, spinnable, heightAdjustable, backseat, armpads):
        Furniture.__init__(self, type, material1, material2, priceTHB)
        self._wheeling = wheeling
        self._spinnable = spinnable
        self._heightAdjustable = heightAdjustable
        self._backseat = backseat
        self._armpads = armpads
    
    def _display(self):
        Furniture._display(self)
        print(f"Wheeling: {self._wheeling}")
        print(f"Spinnable: {self._spinnable}")
        print(f"Height Adjustable: {self._heightAdjustable}")
        print(f"Backseat: {self._backseat}")
        print(f"Armpads: {self._armpads}")

    def __del__(self):
        pass

class Table(Furniture):
    def __init__(self, type, material1, material2, priceTHB, length, width, height, heightAdjustable):
        Furniture.__init__(self, type, material1, material2, priceTHB)
        self._length = length
        self._width = width
        self._height = height
        self._heightAdjustable = heightAdjustable
    
    def _display(self):
        Furniture._display(self)
        print(f"Length: {self._length}")
        print(f"Width: {self._width}")
        print(f"Height: {self._height}")
        print(f"Height Adjustable: {self._heightAdjustable}")

    def __del__(self):
        pass

chair1 = Chair("Dining Chair", "Wood", "Wool", 500, False, False, False, True, False)
chair2 = Chair("Gaming Chair", "Leather", "Steel", 8000, True, True, True, True, True)
chair3 = Chair("Ergonomic Chair", "Wool", "Plastic", 20000, True, True, True, True, True)

table1 = Table("Computer Table", "Wood", "Steel", 2000, 120, 60, 100, False)

chair1._display()
chair2.display()
chair3.display()

table1._display()