m,n = input().split()
m = int(m)
n = int(n)

rule = m,n>= 1 and m,n <= 20
if(rule):
    if(n == m):
        print(n-m)
    elif(n<= m):
        print("No")
    else:
        print(n-m)
    