import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/satislar.csv")

aylar = data[['Aylar']]
satış = data.iloc[:,1:]

x_train,x_test,y_train,y_test = train_test_split(aylar,satış , test_size=0.33, random_state=15)

sc = StandardScaler()
x_train_sc = sc.fit_transform(x_train)
x_test_sc = sc.fit_transform(x_test)
y_train_sc = sc.fit_transform(y_train)
y_test_sc = sc.fit_transform(y_test)

lr = LinearRegression()
lr.fit(x_train_sc, y_train_sc) #x verilerin den y verilerini öğren

tahmin = lr.predict(x_test_sc) #x test verilerine göre y test verilerini tahmin et

x_train_sc = pd.DataFrame(x_train_sc, index=x_train.index).sort_index()
y_train_sc = pd.DataFrame(y_train_sc, index=y_train.index).sort_index()

plt.plot(x_train_sc, y_train_sc)
plt.plot(x_test_sc, tahmin)
plt.show()

'''
Standrat hale getirmediğin trainler için sort uygulaması :
x_train = x_train.sort_index()
y_train = y_train.sort_index()

