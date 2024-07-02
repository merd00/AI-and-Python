from sklearn.preprocessing import StandardScaler
import d_test_and_train_bölme as data

sc = StandardScaler()
x_train_sc = sc.fit_transform(data.x_train)
x_test_sc = sc.fit_transform(data.x_test)

if __name__ == "__main__":
    print("--------------------------------------------------------------------\n x_train_sc:")
    print(x_train_sc)
    print("--------------------------------------------------------------------\n x_test_sc:")
    print(x_test_sc)