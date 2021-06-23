r1,r2 = input().split()
r1 = int(r1)
r2 = int(r2)
result = r1**3 - r2**3
rule = r2>= 1 and r1>= r2 and r1 <=20
if(rule):
    print(result)