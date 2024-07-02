import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
#hunmadity bağımlı

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/odev_tenis.csv")
#print(data)

outlook = data.iloc[:,0:1].values

le = preprocessing.LabelEncoder()
outlook[:,0] = le.fit_transform(outlook[:,0])
#print(outlook)

ohe = preprocessing.OneHotEncoder()
outlook = ohe.fit_transform(outlook).toarray()
#print(outlook)

o = pd.DataFrame(outlook,index=data.index, columns=["overcast","rainy","sunny"])
#print(o)
"""-----------------------------------------------------------------------------------------------"""
windy = data.iloc[:,3:4].values
windy[:,0] = le.fit_transform(windy[:,0])
windy = windy.astype(int)
#print(windy)

w = pd.DataFrame(windy,index=data.index,columns=["windy"])
#print(w)
"""-----------------------------------------------------------------------------------------------"""
play = data.iloc[:,-1:].values
play[:,0] = le.fit_transform(play[:,0])
#print(play)

pl = pd.DataFrame(play,index=data.index,columns=["play"])
"""-----------------------------------------------------------------------------------------------"""
sol = pd.concat([o,data.iloc[:,1:2]],axis=1)
sag = pd.concat([data.iloc[:,3:4],pl],axis=1)

d = pd.concat([sol,sag],axis=1)
humidity = data.iloc[:,2:3].astype(float)
#print(humidity)
#print(d)
"""-------------0----------------------------------------------------------------------------------"""
x = np.append(arr =np.ones((14,1)).astype(float),values = d ,axis=1)
#print(x)

xl = d.iloc[:,[0,1,2,3,4,5]]
xl = np.array(xl,dtype=float)
#print(xl)

model = sm.OLS(humidity,xl).fit()
print(model.summary())

xl = d.iloc[:,[0,1,2,3,5]]
xl = np.array(xl,dtype=float)
#print(xl)

model = sm.OLS(humidity,xl).fit()
print(model.summary())

xl = d.iloc[:,[0,1,3,5]]
xl = np.array(xl,dtype=float)

model = sm.OLS(humidity,xl).fit()
print(model.summary())

model = sm.OLS(humidity,xl).fit()
print(model.summary())

xl = d.iloc[:,[1,3,5]]
xl = np.array(xl,dtype=float)

model = sm.OLS(humidity,xl).fit()
print(model.summary())

xl = d.iloc[:,[1,3]]
xl = np.array(xl,dtype=float)

model = sm.OLS(humidity,xl).fit()
print(model.summary())
"""-------------0----------------------------------------------------------------------------------"""
x_train, x_test, y_train, y_test = train_test_split(d.iloc[:,[0,1,2,3,5]],humidity,test_size=0.33,random_state=0)

lr = LinearRegression()
lr.fit(x_train,y_train)
y_test_predict = lr.predict(x_test)
print(pd.concat((pd.DataFrame(y_test_predict,index = y_test.index,columns = ['humidity predict ']), y_test),axis=1))
"""-------------0----------------------------------------------------------------------------------"""
print("------------------------------------------------------------------------------------------------\n")

x_train, x_test, y_train, y_test = train_test_split(d.iloc[:,[1,3]],humidity,test_size=0.33,random_state=0)

lr = LinearRegression()
lr.fit(x_train,y_train)
y_test_predict = lr.predict(x_test)
print(pd.concat((pd.DataFrame(y_test_predict,index = y_test.index,columns = ['humidity predict ']), y_test),axis=1))