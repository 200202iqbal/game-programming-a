#試験の合格判定 
loop = int(input())
rule = loop >= 1 and loop <= 1000
count = 0
if(rule):
    for _ in range(loop):
        inputdata = input().split()
        codeuniq = str(inputdata[0])
        if(codeuniq == "s" or "l"):
            totalresult = int(inputdata[1])+int(inputdata[2])+int(inputdata[3])+int(inputdata[4])+int(inputdata[5])
            if(codeuniq == "s" and totalresult >= 350):
                result = int(inputdata[2]) + int(inputdata[3])
                if(result >= 160):
                    count +=1
            elif(codeuniq == "l" and totalresult >= 350):
                result = int(inputdata[4]) + int(inputdata[5])
                if(result >= 160):
                    count +=1;

print(count)
            
        