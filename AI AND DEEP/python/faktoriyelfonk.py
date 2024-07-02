def fakhesapla(x):
    if x < 0 :
        print("negatif sayıların faktoriyeli olamaz")
        exit(0)
    if x == 0:
        print("Sonuç: 1")
        exit(0)
    sum = 1
    for i in range(1,x+1):
        sum = sum * i
    return print("Sonuç:",sum)

x = int(input("faktoriyelini hesaplamak istediğiniz sayıyı giriniz: "))
fakhesapla(x)
