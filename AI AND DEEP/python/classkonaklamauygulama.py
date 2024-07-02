
class konkalama():
    def __init__(self,konaklamaisim,konum,oda):
        self.konaklamaisim=konaklamaisim
        self.konum=konum
        self.oda=oda
        self.rezerveoda = None
        self.rezervasyon = []

    def rezervasyonyap(self,oda,müşteri):
            if oda <= self.oda:
                self.rezerveoda = oda
                self.oda -= oda
                self.rezervasyon.append(müşteri)
                print("rezervasyon başarılı")

            elif oda > self.oda:
                self.müşteri = müşteri
                print(f"Sayın {self.müşteri}, istediğiniz sayıda oda bulunamadı, rezervasyon başarısız")

    def rezerveeden(self):
        for rezervasyon in self.rezervasyon:
            pass
        print(f"{self.rezerveoda} oda tarafınıza ayrılmıştır, sayın {self.rezervasyon[-1]}")

    def kalanodasayısı(self):
        if self.oda == 0:
            print(f"{self.konaklamaisim} yerleşkesinde boş odamız bulunmamaktadır.")
        else:
            print( f"{self.konaklamaisim} yerleşkesinde boş oda sayısı: {self.oda}")



otel = konkalama("GRAND PLACE","İZMİR",4)

otel.kalanodasayısı()
otel.rezervasyonyap(3,"mert öztürk")
otel.rezerveeden()
otel.kalanodasayısı()
otel.rezervasyonyap(1,"cenk öztürk")
otel.rezerveeden()
otel.rezervasyonyap(6,"zügürt aga")
otel.kalanodasayısı()



