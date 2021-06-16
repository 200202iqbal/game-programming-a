n,d,e = input().split()
n = int(n)
d = int(d)
e = int(e)
result = d*e
rule = n,d,e >= 1 and n <= 500 and d<=10 and e<=500
if(rule):
    if(n <= result):
        print("OK")
    else:
        print("NG")