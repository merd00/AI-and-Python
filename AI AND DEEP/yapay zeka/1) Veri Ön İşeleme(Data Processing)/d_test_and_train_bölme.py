import c_sonucları_dataframde_toplama as data
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data.numaricresult,data.result3, test_size=0.33, random_state=0)
if __name__ == "__main__":
    print(x_train)
    print(x_test)
    print(y_train)
    print(y_test)