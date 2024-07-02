class person:
    def __init__(self,name,lastname,e_mail):
        self.name = name
        self.lastname = lastname
        self.e_mail = e_mail

    def __str__(self):
        return f"İsim : {self.name}, Soyisim: {self.lastname }, Mail: {self.e_mail}"

class VIPperson(person):
    def __init__(self,name,lastname,e_mail,sale):   #ekstra bir şeyler tanımlandığı için kullanılır.(sale)
        super().__init__(name,lastname,e_mail)      #eklenmek istenen ekstra bir şey yok ise direk aşşağı fonk a atlanabilir.
        self.sale = sale

    def vipbilgi(self):
        return super().__str__() ,  f"Vip Müşteri için indirim oranı : {self.sale}"


vip1 = VIPperson("cenk","öztürk","cengoo@mail.com", "%60")
person1 = person("mert","keleş","mertk_ak47@mail.com")

print(vip1.vipbilgi())
print(person1)