import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/maaslar_yeni.csv")
print(data)

y = data.iloc[:,5:]
y_value = y.values
x1 = data.iloc[:,2:3]
x2 = data.iloc[:,4:5]
x = pd.concat([x1,x2], axis=1)
x_value = x.values

#random forest
rf = RandomForestRegressor(n_estimators=31, random_state=0)
rf.fit(x_value,y_value.ravel())

model = sm.OLS(rf.predict(x_value),x_value).fit()
print(model.summary(),"\n")

rf_başarı = r2_score(y_value, rf.predict(x_value))
print(f"random forest başarısı: {rf_başarı}")

print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

#polynomial regression
poly = PolynomialFeatures(degree=5)
x_poly = poly.fit_transform(x_value)

lr = LinearRegression()
lr.fit(x_poly,y_value.ravel())

model = sm.OLS(lr.predict(x_poly),x_value)
print(model.fit().summary(),"\n")


poly_başarı = r2_score(y_value, lr.predict(x_poly))
print(f"poly regression başarısı: {poly_başarı}")

print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# linear regression
lr2 = LinearRegression()
lr2.fit(x_value,y_value)

model = sm.OLS(lr2.predict(x_value),x_value)
print(model.fit().summary(),"\n")

lr_başarı = r2_score(y_value, lr2.predict(x_value))
print(f"linear regression başarısı: {lr_başarı}")

print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

#support vector regression
scl1 = StandardScaler()
scl2 = StandardScaler()
x_sc = scl1.fit_transform(x_value)
y_sc = np.ravel(scl2.fit_transform(y_value.reshape(-1,1)))

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_sc,y_sc)

model = sm.OLS(svr_reg.predict(x_sc),x_sc)
print(model.fit().summary(),"\n")

svc_başarı = r2_score(y_sc, svr_reg.predict(x_sc))
print(f"SVC regression başarısı: {svc_başarı}")

print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Decision Tree
dt = DecisionTreeRegressor(random_state=0)
dt.fit(x_value,y_value.ravel())

model = sm.OLS(dt.predict(x_value),x_value)
print(model.fit().summary(),"\n")

dt_başarı = r2_score(y_value, dt.predict(x_value))
print(f"decision tree başarısı: {dt_başarı}")

print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")
