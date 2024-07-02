"""TÜM DEĞERLERİ (SUTUNLARI) KULLANDIĞIM İÇİN TAHMİNLER ÇOĞUNUNLUKLA YANLIŞ VEYA HATA ORANI YÜKSEK BİR ŞEKİLDE ÇIKTI
SADECE MULTİ LİNEAR REGRESSİON U ANLAMAK AMAÇLI BİR KOD DİZİNİDİR.
NOT: SADECE DUMMY DEĞERLERDEN KAÇINILDI."""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

data = pd.read_csv("C:/Users/mertt/OneDrive/Masaüstü/AI AND DEEP/veriler/veriler.csv")
#print(data)

country = data.iloc[:,0:1].values

le = preprocessing.LabelEncoder()
country[:,0] = le.fit_transform(data.iloc[:,0])

ohe = preprocessing.OneHotEncoder()
country = ohe.fit_transform(country).toarray()
#print(country)

sex = data.iloc[:,-1:].values
sex[:,0] = le.fit_transform(data.iloc[:,-1])
sex = ohe.fit_transform(sex).toarray()  #kolumları alfabetik sıraya göre yazar önce e sonra k
#print(sex)

s1 = pd.DataFrame(data=country, index=data.index, columns=['fr','tr','us'])
#print(s1)

sayısalveriler = data.iloc[:,1:4]
s2 = pd.DataFrame(data = sayısalveriler)
#print(s2)

s3dummy = pd.DataFrame(data=sex, index=data.index, columns=['e','k']) #erkek olmak veya kadın olmak birbiri ile ilişkili olduğundan
#print(s3)                                                            #dummy varible oluşturur bu yüzden birini seçmemiz gerekir
s3 = pd.DataFrame(data = s3dummy, index=data.index, columns=['e'])

change_data = pd.concat([s1, s2], axis=1)
#print(change_data)

all_data = pd.concat([change_data, s3], axis=1)
#print(all_data.head())

#cinsiyet tahmin
xs_train, xs_test, ys_train, ys_test = train_test_split(change_data,s3, test_size=0.33, random_state=0)

sc = StandardScaler()
xs_train_sc = sc.fit_transform(xs_train)
ys_train_sc = sc.fit_transform(ys_train)
xs_test_sc = sc.fit_transform(xs_test)
ys_test_sc = sc.fit_transform(ys_test)

lr = LinearRegression()
lr.fit(xs_train_sc, ys_train_sc)
predict_ys_test_sc = lr.predict(xs_test_sc)

print(pd.concat([pd.DataFrame(predict_ys_test_sc,index=ys_test.index,columns=['erkek mi tahmin']),
                 pd.DataFrame(ys_test_sc,index =ys_test.index)],axis=1).sort_index())

print("*********************************************************************************************")
#cinsiyetin standardize edilmemiş hali
lr.fit(xs_train, ys_train)
predict_ys_test = lr.predict(xs_test_sc)

print(pd.concat([pd.DataFrame(predict_ys_test,index=ys_test.index,columns=['erkek mi tahmin']),ys_test],axis=1).sort_index())

print("*********************************************************************************************")
# boy kolonunu çekip onu tahmin ettirmek
boy = all_data.iloc[:,3:4]
left = all_data.iloc[:,0:3]
right = all_data.iloc[:,4:]

boysuz_data = pd.concat([left, right], axis=1)

xb_train, xb_test, yb_train, yb_test = train_test_split(boysuz_data,boy, test_size=0.33, random_state=0)

lr.fit(xb_train, yb_train)
predict_yb_test = lr.predict(xb_test)

print(pd.concat([pd.DataFrame(predict_yb_test,index=yb_test.index,columns=['boy tahmin']),yb_test],axis=1).sort_index())

