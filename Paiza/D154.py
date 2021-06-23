n = int(input())
m = int(input())
rule= m>=0 and n * n >= m
if(rule):
    result = n*n-m
    print(result)