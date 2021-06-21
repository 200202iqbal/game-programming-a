n = int(input())
rule = n >=100 and n<=999

if(rule):
    n=str(n)
    if(n[0] == "2"):
        print("ok")
    elif(n[0]== "4"):
        print("error")
    else:
        print("unknown")