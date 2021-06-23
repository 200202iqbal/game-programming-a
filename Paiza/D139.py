loop = int(input())
i = 0
inputA = input().split()
keyG = 0
keyP = 0
rule = loop >= 3 and loop<=100 and len(inputA) >= 1 and len(inputA)<= loop
if(rule):
    for key in inputA:
        if(key == "G" or key == "P"):
            if(key =="G"):
                keyG +=1
            else:
                keyP +=1
    if(keyG > keyP):
        print("P")
    elif(keyG < keyP):
        print("G")
    else:
        print("Draw")
    