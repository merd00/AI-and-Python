import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/eksikveriler.csv")

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = data.iloc[:,1:4].values #1den4 e kadar olan sutunların her satırındaki değerleri verir liste içinde

imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
country = data.iloc[:,0:1].values

le = preprocessing.LabelEncoder()
country[:,0] = le.fit_transform(country[:,0])

ohe = preprocessing.OneHotEncoder()
country = ohe.fit_transform(country).toarray()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#DataFrame oluşturup birleştirme kısmı
if __name__ == "__main__":
    print(data.index)

result1 = pd.DataFrame(data=country, index=data.index, columns=['fr','tr','us'])
if __name__ == "__main__":
    print(result1)

result2 = pd.DataFrame(data=yas, index=data.index, columns=['boy','kilo','yas'])
if __name__ == "__main__":
    print(result2)

result3 = pd.DataFrame(data=data.iloc[:,-1], index=data.index, columns=['cinsiyet'])
if __name__ == "__main__":
    print(result3)

numaricresult = pd.concat([result1, result2], axis=1)
if __name__ == "__main__":
    print(numaricresult)

result = pd.concat([result1, result2, result3], axis=1)
if __name__ == "__main__":
    print(result)
