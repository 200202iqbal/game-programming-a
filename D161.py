n = int(input())
loop = 7
quantity = 0
rule = n >=1 and n<=1000
if(rule):
    while(loop > 0):
        waterDay = int(input())
        quantity += waterDay
        loop -= 1
        if(quantity > n):
            quantity = n
print(quantity)