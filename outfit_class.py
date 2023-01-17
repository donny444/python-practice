class outfit:
    def __init__(self, hat, glasses, top, bottom, watch, bracelet, socks, shoes, outerwear, underwear):
        self.hat = hat
        self.glasses = glasses
        self.top = top
        self.bottom = bottom
        self.watch = watch
        self.bracelet = bracelet
        self.socks = socks
        self.shoes = shoes
        self.outerwear = outerwear
        self.underwear = underwear
    def myShoes(self):
        print("My shoes of the outfit: " + self.shoes)
o1 = outfit("-","-","-","-","-","-","-","-","-","-")
o1.hat = None
o1.glasses = None
o1.top = "INDVLST"
o1.bottom = "UNIQLO Blue Jean"
o1.watch = "DENIM G-SHOCK"
o1.bracelet = None
o1.socks = "Neon Green RIPNDIP"
o1.shoes = "Nike AF1 Black Taxi"
o1.outerwear = None
o1.underwear = "UNIQLO White"
o1.myShoes()