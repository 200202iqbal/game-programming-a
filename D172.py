a,n = input().split()
a = int(a)
n = int(n)
rule = a >=1 and a<=2000 and n >=1 and n<=20
if(rule):
    result = a * n
    print(result)