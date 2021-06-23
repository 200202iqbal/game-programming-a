inputRain = input().split()

rule = inputRain == 0 or 1
rainstatus = 0
for i in inputRain:
    if(int(i) == 1 or int(i) == 0):
        if(int(i) == 1):
            rainstatus += 1
 
if(rainstatus >= 5):
    print("yes")
else:
    print("no")

    