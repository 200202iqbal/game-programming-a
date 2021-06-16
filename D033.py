s,t = input().split()
s = str(s)
t = str(t)
s = s.upper()
t = t.upper()
slen = len(s)
tlen = len(t)
rule = slen,tlen >= 2 and slen,tlen <=20
result = s[0]+"."+t[0]
if(rule):
    print(result)
