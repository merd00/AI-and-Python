cümle = input("sıralamk istediğiniz cümleyi girin: ")

kelimeler = cümle.split()
print(kelimeler)

sırala = kelimeler.sort()

for i in kelimeler:
    print(i)

#ç ingilizce karakter olmadığı için sıralamada sona atılır. 


