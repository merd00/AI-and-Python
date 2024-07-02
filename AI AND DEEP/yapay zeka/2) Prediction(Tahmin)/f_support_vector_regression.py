import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/maaslar.csv")

x = data.iloc[:,1:2]
y = data.iloc[:,2:]
x_val = x.values
y_val = y.values

slc = StandardScaler()
x_scaler = slc.fit_transform(x_val)

slc1 = StandardScaler()
y_scaler = np.ravel(slc1.fit_transform(y_val.reshape(-1,1))) # değerleri yan yana yazdırır
#print(x_scaler)
#print(y_scaler)

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_scaler, y_scaler)

plt.scatter(x_scaler, y_scaler)
plt.plot(x_scaler, svr_reg.predict(x_scaler))
plt.show()

print(svr_reg.predict([[11]]))
