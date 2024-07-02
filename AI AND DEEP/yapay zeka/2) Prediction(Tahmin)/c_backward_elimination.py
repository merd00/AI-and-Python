import pandas as pd
from sklearn import preprocessing #ENCODER
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import statsmodels.api as sm


data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/veriler.csv")
#print(data.head())

country = data.iloc[:,0:1].values
le = preprocessing.LabelEncoder()
country[:,0]=le.fit_transform(country[:,0])

ohe = preprocessing.OneHotEncoder()
country = ohe.fit_transform(country).toarray()
#print(country)

sex = data.iloc[:,-1:].values
sex[:,0] = le.fit_transform(country[:,0])
#print(sex)

c = pd.DataFrame(country,index = data.index, columns = ['FR','TR','US'])
s = pd.DataFrame(sex,index=data.index,columns=['cinsiyet'])
multi_data = data.iloc[:,1:4]

d = pd.concat([c,multi_data],axis=1,)
#print(d)
new_data = pd.concat([d,s],axis=1,)
#print(new_data)

cinsiyet = s.iloc[:,0].values.astype(float) #ndarray halinde olması gerek
#print(type(cinsiyet))

print(new_data.index)

x = np.append(arr = np.ones((22,1)).astype(int), values = d, axis = 1)
#print(x)

x_l = d.iloc[:,[0,1,2,3,4,5]].values
x_l = np.array(x_l,dtype=float)
model = sm.OLS(cinsiyet,x_l).fit()
print(model.summary())

x_l = d.iloc[:,[0,2,3,4,5]].values
x_l = np.array(x_l,dtype=float)
model = sm.OLS(cinsiyet,x_l).fit()
print(model.summary())

x_l = d.iloc[:,[0,3,4,5]].values
x_l = np.array(x_l,dtype=float)
model = sm.OLS(cinsiyet,x_l).fit()
print(model.summary())

x_l = d.iloc[:,[0,4,5]].values
x_l = np.array(x_l,dtype=float)
model = sm.OLS(cinsiyet,x_l).fit()
print(model.summary())

x_l = d.iloc[:,[0]].values
x_l = np.array(x_l,dtype=float)
model = sm.OLS(cinsiyet,x_l).fit()
print(model.summary())

"""P değeri büyük olanları çıkartarak en doğru sütun seçimine ulaşmak gerekli bu yüzden elemeler yaparak her elemeden sonra 
sonuçlara göz atıp doğru kombinasyonu kurmalıyız. En son ise regresyon işlemine başlamalıyız. """

verimli_data = d.iloc[:,[0,4,5]]
x_train, x_test, y_train, y_test = train_test_split(verimli_data,s,test_size=0.33, random_state=42)

lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)

print(pd.concat([pd.DataFrame(y_pred,index=y_test.index,columns=['cinsiyet tahmin']),
                 pd.DataFrame(y_test,index =y_test.index)],axis=1).sort_index())

print("-----------------------------------------------------")

verimli_data = d.iloc[:,[0]]
x_train, x_test, y_train, y_test = train_test_split(verimli_data,s,test_size=0.33, random_state=42)

lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)

print(pd.concat([pd.DataFrame(y_pred,index=y_test.index,columns=['cinsiyet tahmin']),
                 pd.DataFrame(y_test,index =y_test.index)],axis=1).sort_index())
