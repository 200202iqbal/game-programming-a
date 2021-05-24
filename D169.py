h,l = input().split()
h = int(h)
l = int(l)
rule = l<=h and l,h>=0 and l,h<=35
if(rule):
    print(h-l)