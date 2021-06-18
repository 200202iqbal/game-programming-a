s = input()

rule = len(s)>=1 and len(s)<=20
if(rule):
    for i in s:
       sn = int(i)
    if(sn == 1):
        slen= len(s)
        if(slen<11):
            print(11-slen)
        else:
            print("OK")