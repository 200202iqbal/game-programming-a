n =int(input())
rule = n>=1 and n<=100
if(rule):
    sn = str(n)
    sn = sn.zfill(3)
    print(sn)