d = input().split()
finalresult=0
result=0
for i in d:
    if(int(i) >= 1 and int(i)<= 1000):
        if(int(i)>5):
            result = 5
        else:
            result = int(i)
    finalresult += result
print(finalresult)