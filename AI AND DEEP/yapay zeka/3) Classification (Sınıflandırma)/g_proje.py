import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

data = pd.read_excel("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/Iris.xls") #XLRD KÜTÜP YÜKLENMELİ
print(data)

x = data.iloc[:, 0:4].values
y = data.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

scl = StandardScaler()
x_train_sc = scl.fit_transform(x_train)
x_test_sc = scl.transform(x_test)

svc = SVC(kernel='rbf')
svc.fit(x_train_sc, y_train)
cm1 = confusion_matrix(y_test, svc.predict(x_test_sc))
print("svc confusion matrix:\n",cm1)

knn = KNeighborsClassifier(n_neighbors=5,metric='minkowski')
knn.fit(x_train, y_train)
cm2 = confusion_matrix(y_test, knn.predict(x_test))
print("knn confusion matrix:\n",cm2)

lgr = LogisticRegression()
lgr.fit(x_train, y_train)
cm3 = confusion_matrix(y_test, lgr.predict(x_test))
print("lgr confusion matrix:\n",cm3)

nbg = GaussianNB()
nbg.fit(x_train, y_train)
cm4 = confusion_matrix(y_test, nbg.predict(x_test))
print("nbg confusion matrix:\n",cm4)

dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(x_train, y_train)
cm5 = confusion_matrix(y_test, dt.predict(x_test))
print("dt confusion matrix:\n",cm5)

rf = RandomForestClassifier(n_estimators=10,criterion='entropy')
rf.fit(x_train, y_train)
cm6 = confusion_matrix(y_test, rf.predict(x_test))
print("rf confusion matrix:\n",cm6)

#roc

y_proba_rf = rf.predict_proba(x_test_sc)

print("roc:")
fpr , tpr , thresholds = metrics.roc_curve(y_test, y_proba_rf[:,0],pos_label="Iris-setosa")
print("fpr:",fpr,"tpr:",tpr,"thresholds:",thresholds)