import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/maaslar.csv")

x = data.iloc[:,1:2]
y = data.iloc[:,2:]
x_val = x.values
y_val = y.values

poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(x_val)

lin_reg = LinearRegression()
lin_reg.fit(x_poly, y_val)

plt.scatter(x_val,y_val)
plt.plot(x_val,lin_reg.predict(x_poly))
plt.show()

poly_reg = PolynomialFeatures(degree = 5)
x_poly = poly_reg.fit_transform(x_val)

lin_reg = LinearRegression()
lin_reg.fit(x_poly, y_val)

print(data)
print(lin_reg.predict(poly_reg.fit_transform([[4.5]])))
print(lin_reg.predict(poly_reg.fit_transform([[11]])))

plt.scatter(x_val,y_val)
plt.plot(x_val,lin_reg.predict(x_poly))
plt.show()