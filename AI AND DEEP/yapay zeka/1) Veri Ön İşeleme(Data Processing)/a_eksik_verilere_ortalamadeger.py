import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/eksikveriler.csv")

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = data.iloc[:,1:4].values #1den4 e kadar olan sutunların her satırındaki değerleri verir liste içinde

imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])

print(yas)


'''  CSV DOSYASI İMPORTLAMAK VE BİR SATIR ÇEKMEK
data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/veriler.csv")

print(data)

cinsiyetveboy = data[['cinsiyet',"boy"]]
print(cinsiyetveboy)

'''




