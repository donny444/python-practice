class Computer:

    def __init__(self, cpu, gpu, mb, ram, psu, case):
        self.cpu = cpu
        self.gpu = gpu
        self.mb = mb
        self.ram = ram
        self.psu = psu
        self.case = case
    def __str__(self):
        return f"CPU: {self.cpu}\nGPU: {self.gpu}\nMainboard: {self.mb}\nRAM: {self.ram}\nPower Supply: {self.psu}\nCase: {self.case}"

class Setup(Computer):
    def __init__(self, cpu, gpu, mb, ram, psu, case, keyboard):
        super().__init__(cpu, gpu, mb, ram, psu, case)
        self.keyboard = keyboard
    def findKeyboard(self):
        print("The keyboard is " + self.keyboard)

myPc = "---My Desktop---\n" + str(Computer("I5-8400","GTX 1070Ti","H370 HD3",None,"CV650","H500"))
dreamPc = Setup(None,"RTX 3090",None,"32GB","CX750M","H900","G512")
print(myPc)
dreamPc.findKeyboard()