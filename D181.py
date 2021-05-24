n1 = int(input())
n2 = int(input())
n3 = int(input())
rule = n1,n2,n3 >= 1 and n1,n2,n3<=9999

if(rule):
    print(n1,end="-")
    print(n2,end="-")
    print(n3)