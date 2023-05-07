class Chair:
    def __init__(self, type, material_1, material_2, price):
        self.__type = type
        self.__material_1 = material_1
        self.__material_2 = material_2
        self.__price = price
    
    def display(self):
        print(f"Chair type: {self.__type}")
        print(f"Chair 1st material: {self.__material_1}")
        print(f"Chair 2nd material: {self.__material_2}")
        print(f"Chair Price: {self.__price}")

    def __del__(self):
        pass

ob_j1 = Chair("Dining Chair", "Wood", "Wool", 5000)