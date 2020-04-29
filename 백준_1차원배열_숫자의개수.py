multiple=1
for i in range(3):
    a=int(input())
    multiple=multiple*a
num=str(multiple)
for i in range(0,10):
    print(num.count(str(i)))
