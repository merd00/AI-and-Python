import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/maaslar.csv")

x = data.iloc[:,1:2]
y = data.iloc[:,2:]
x_val = x.values
y_val = y.values

rf_reg = RandomForestRegressor(n_estimators=10,  random_state=0)
rf_reg.fit(x_val, y_val.ravel())

print(rf_reg.predict([[4.5]]))

plt.scatter(x_val,y_val)
plt.plot(x_val,rf_reg.predict(x_val))
plt.show()