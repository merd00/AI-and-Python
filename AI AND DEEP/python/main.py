x = int(input("Enter a number: "))
flag = 0

if x == 1 or x == 2 :
    print("x not asal")

for i in range(3,x):
    if x % 2 == 0:
        print("x not asal")
        flag = 1 
        break
    if x%i == 0:
        print("x not asal")
        flag = 1
        break
    i = i + 1

if flag == 0:
    print("x asal")