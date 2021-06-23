y,m,d = input().split()
y = int(y)
m = int(m)
d = int(d)

rule = y >= 2000 and y <= 2016 and m >= 1 and m<= 12 and d >= 1 and d <= 31
if(rule):
    print(y,end="/")
    print(m,end="/")
    print(d)