def sayıgir():
    a = int(input("ilk sayıyı girin "))
    b = int(input("ikinci sayıyı girin "))
    return a,b

x = int(input("yapmak istediğiniz işlemin numarısını girin "
              "( 1 : Toplama, 2 : Çıkarma, 3 : Çarpma, 4 : Bölme ) :"))

if x == 1:
    a,b = sayıgir()
    result = a + b
    print("toplamın sonucu : ",result)

elif x == 2:
    a, b = sayıgir()
    result = a - b
    print("çıkarmanın sonucu : ", result)

elif x == 3:
    a, b = sayıgir()
    result = a * b
    print("çarpımın sonucu : ", result)

elif x == 4:
    a, b = sayıgir()
    result = a / b
    print("bölümün sonucu : ", result)

else:
    print("yanlış operasyon girdiniz lütfen tekrar deneyin ")
