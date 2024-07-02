import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/maaslar.csv")

x = data.iloc[:,1:2]
y = data.iloc[:,2:]
x_val = x.values
y_val = y.values

dt_reg = DecisionTreeRegressor(random_state=0)
dt_reg.fit(x_val, y_val)

plt.scatter(x_val, y_val)
plt.plot(x_val, dt_reg.predict(x_val))
plt.show()

print(data)
print(dt_reg.predict([[11]]))
print(dt_reg.predict([[4.5]]))