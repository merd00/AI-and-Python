def matrixgir():
    m = (int(input("matrixiniz yatay uzunluğunu giriniz: ")))
    n = (int(input("matrixiniz dikey uzunluğunu giriniz: ")))
    x = []

    for i in range(m):
        yatay = []
        for j in range(n):
            v = int(input(f"elemanları girin {[i+1]}{[j+1]}: "))
            yatay.append(v)
        x.append(yatay)
    return x

def matrixtopla(x,y):
    sonuç = []
    for i in range(len(x)):
        summer = []
        for j in range(len(y)):
            summer.append( x[i][j] + y[i][j])
        sonuç.append(summer)

    return sonuç

matrix1 = matrixgir()
matrix2 = matrixgir()
print(matrixtopla(matrix1,matrix2))

