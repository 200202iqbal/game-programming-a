a,b = input().split()
a = int(a)
b = int(b)

rule = a,b >= 1 and a,b <=1000
if rule:
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("eq")