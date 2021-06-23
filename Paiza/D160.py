n = int(input())
m = int(input())
result = (n//10) * m
rule = n>=10 and n<=5000 and m>=1 and m<=10
if(rule):
    print(result)