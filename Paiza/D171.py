p1,p2 = input().split()
target = int(input())
p1 = int(p1)
p2 = int(p2)

rule = p1,p2 >= 1 and p1,p2<=100
if(rule):
    p1result = p1 - target
    p2result = p2 - target
    print(p1result,p2result)
