number = input().split()
i = 0 
while (i< len(number)):
    number[i] = int(number[i])
    i += 1
finalresult = 0
for n in number :
    result = 1
    rule = n >=1 and n <=13
    if(rule):
        result *= n
        finalresult += result
if(finalresult < 16):
    print("HIT")
else:
    print("STAND")