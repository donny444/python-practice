class alien:
    def __init__ (self, color, body, planet):
        self.color = color
        self.body = body
        self.planet = planet

class avatar(alien):
    def __init__ (self, color, body, planet, tribe)
        self.tribe = tribe

        alien.__init__(self, color, body, planet)

    def display(self)
        print()