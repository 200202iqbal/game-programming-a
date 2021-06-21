n = int(input())
rule = n>=1 and n<=100
n = range(n+1)
b = 0
if(rule):
    for i in n:
        a = i
        b += a
    print(b)