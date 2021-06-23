t,u =input().split()
t = int(t)
u = int(u)
result = t - u
rule = t,u >=-40 and t,u <=40 and u < t
if(rule):
    print(result)