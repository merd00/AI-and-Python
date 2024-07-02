import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/veriler.csv")

x = data.iloc[:, 1:4].values
y = data.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

rf = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
rf.fit(x_train, y_train)
y_pred = rf.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)

print(y_test,"\n",y_pred)
