n1,n2 = input().split()
n3,n4 = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)

rule = n1,n2,n3,n4 >= -1000 and n1,n2,n3,n4 <= 1000
if rule:
    print((n1*n4) - (n2*n3))