n,m = input().split()
n = int(n)
m = int(m)
result = n//m
rule = n>= 0 and m >=1 and n,m<=100
if(rule):
    print(result)