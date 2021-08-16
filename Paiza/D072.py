x,y,p = input().split()
x = int(x) #banyaknya data yg ingin disimpan (GB)
y = int(y) #banyaknya kapasistas yang bisa ditampung
p = int(p) # harga hardisk

rule = x,y,p >= 1 and x,y <=1000 and p <= 10000
if rule:
    count = 0
    total = 0
    while  total < x:
        total +=y
        count +=1
    price = count * p
    print(price)