class sporcu:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.exercise= None
        self.health = None

    def addhealth(self,healthinformation):
        self.health = healthinformation

    def addexercise(self,exerciseinformation):
        self.exercise = exerciseinformation

    def showinformation(self):
        return f"{self.name}  {self.lastname} - {self.age} - {self.exercise} - {self.health}"

class healthinformation:
    def __init__(self,weight,height,pulse,bloodpressure):
        self.weight = weight
        self.height = height
        self.pulse = pulse
        self.bloodpressure = bloodpressure

    def __str__(self):
        return f"weight: {self.weight}, height: {self.height}, pulse= {self.pulse}, bloodpressure {self.bloodpressure}"

class exerciseinformation:
    def __init__(self,program):
        self.program = program

    def __str__(self):
        return f"Exercises: {self.program}" # {', '.join(self.program)} liste formatından çıkarıp string olarak sıralar.



sprocu1 = sporcu("Mert", "Öztürk",23)
sprocu1exercise = exerciseinformation(["Esneme", "Isınma", "Koşu", "Ağırlık", "Soğuma"])
sprocu1health = healthinformation(100, 183, 99, [13.7])

sprocu1.addexercise(sprocu1exercise)
sprocu1.addhealth(sprocu1health)
print(sprocu1.showinformation())