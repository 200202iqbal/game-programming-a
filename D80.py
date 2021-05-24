n,m = input().split()
n = int(n)
m = int(m)
result = n * 6000 + m*4000
rule = n,m >= 1 and n,m<=100
if(rule):
     print(result)
