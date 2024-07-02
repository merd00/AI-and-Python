class etkinlik:
    def __init__(self,name,date,place):
        self.name = name
        self.date = date
        self.place = place
        self.ticket = []

    def addticket(self,ticket):
        self.ticket.append(ticket)

    def showticket(self):
        for ticket in self.ticket:
            print(ticket)

class ticket:
    def __init__(self,cat,price,reserve):
        self.cat = cat
        self.price = price
        self.reserve = reserve

    def __str__(self):
        return f"{self.cat}  , {self.price} , Reserve's name =  {self.reserve}"

konser = etkinlik("2Pac RIP","24.06.2024","ANKARA" )
print(konser.name)
print(konser.date)
print(konser.place)

ticket1 = ticket(cat="A",price=10,reserve="mert")
print(ticket1)
ticket2 = ticket(cat="B",price=20,reserve="cenk")
print(ticket2, "\n-------------------------------------")

konser.addticket(ticket1)
konser.addticket(ticket2)
konser.showticket()