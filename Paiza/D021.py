#文字列の一致
s = str(input())
t = str(input())

rule = len(s),len(t) >= 1 and len(s),len(t) <=10
if(rule):
    if(s == t):
        print("Yes")
    else:
        print("No")