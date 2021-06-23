#脱出ゲーム
inputs = input()
rule = len(inputs)>=1 and len(inputs)<=100 and int(inputs) == 0,1,2
if(rule):
    for _ in inputs:
        s = int(_)
        if(s == 0):
            print("C",end="")
        elif(s == 1):
            print("A",end="")
        elif(s == 2):
            print("B",end="")