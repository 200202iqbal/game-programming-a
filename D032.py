n = int(input())
rule = n>=0 and n<=100
charge = 100 - n
if(rule):
    print(charge)