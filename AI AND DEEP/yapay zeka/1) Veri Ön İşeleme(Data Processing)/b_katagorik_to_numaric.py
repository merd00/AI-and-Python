from sklearn import preprocessing
import pandas as pd

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/eksikveriler.csv")

country = data.iloc[:,0:1].values
print(country)

le = preprocessing.LabelEncoder()
country[:,0] = le.fit_transform(country[:,0])
print(country)

ohe = preprocessing.OneHotEncoder()
country = ohe.fit_transform(country).toarray()
print(country)