c,t,a = input().split()
c = int(c)
t = int(t)
a = int(a)
result= (c+t+a)
rule = c,t,a >= 1 and c,t,a <=10
if(rule):
    print(result)