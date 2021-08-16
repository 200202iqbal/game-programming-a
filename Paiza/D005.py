m,n = input().split()
m = int(m)
n = int(n)
result = [m,]
rule = m,n >= 1 and m,n <= 100
if rule:
    count = 9
    while count > 0:
        m += n
        result.append(m)
        count -=1
    print(*result)
        
    
        