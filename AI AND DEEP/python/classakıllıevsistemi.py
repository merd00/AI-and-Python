class smartdevices:
    def __init__(self,place):
        self.place=place
        self.status = False

    def open(self):
        self.status = True

    def close(self):
        self.status = False

class light(smartdevices):
    def __init__(self,place,color):
        super().__init__(place)
        self.color = color

    def changecolor(self, new_color):
        self.color = new_color

class airconditioner(smartdevices):
    def __init__(self,place,temp):
        super().__init__(place)
        self.temp = temp

    def changetemp(self, new_temp):
        self.temp = new_temp

class coffemaker(smartdevices):
    pass

light1 = light("bedroom", "white")
airconditioner1 = airconditioner("live room", 22)
coffemaker1 = coffemaker("kitchen")

light1.changecolor("Red")
airconditioner1.changetemp(19)
coffemaker1.open()
light1.open()
airconditioner1.open()

print(coffemaker1.status)
print(light1.color)
print(airconditioner1.temp)