class alien:
    def __init__ (self, color, body, planet):
        self._color = color
        self._body = body
        self._planet = planet

        self._display()

    def _display(self):
        print("This alien have {} skin color".format(self._color))
        print("This alien have {} body type".format(self._body))
        print("This alien from {} ".format(self._planet))

class avatar(alien):
    def __init__ (self, color, body, planet, tribe):
        self._tribe = tribe

        alien.__init__(self, color, body, planet)

        print("This alien is in {} tribe".format(self._tribe))

class titan(alien):
    def __init__ (self, color, body, planet, deviant):
        self._deviant = deviant

        alien.__init__(self, color, body, planet)

        print("Deviant statement: {}".format(self._deviant))

jakesully = avatar("Blue", "Tall", "Pandora", "Jungle")
print("\n")
thanos = titan("Purple", "Big", "Titan", str(True))