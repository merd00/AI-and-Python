import pandas as pd
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/maaslar.csv")

x = data.iloc[:,1:2]
y = data.iloc[:,2:]
x_val = x.values
y_val = y.values

rf_reg = RandomForestRegressor(n_estimators=10,  random_state=0)
rf_reg.fit(x_val, y_val.ravel())

sorgu = r2_score(y_val, rf_reg.predict(x_val)) #başarı oranı belirler
print(sorgu)

