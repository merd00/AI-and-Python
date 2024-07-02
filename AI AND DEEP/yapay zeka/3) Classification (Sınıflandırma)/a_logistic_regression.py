import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/veriler.csv")
#print(data)

x = data.iloc[:, 1:4].values
y = data.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

lgr = LogisticRegression(random_state=0)
lgr.fit(x_train, y_train)

y_pred = lgr.predict(x_test)
print(y_pred)
print(y_test.ravel())

cm = confusion_matrix(y_test, y_pred)
print(cm)