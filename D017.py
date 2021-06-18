n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

rule = n1,n2,n3,n4,n5 >= 1 and n1,n2,n3,n4,n5 <=99
if(rule):
    n = [n1,n2,n3,n4,n5]
    print(max(n))
    print(min(n))