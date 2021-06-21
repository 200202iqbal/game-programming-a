string = input()
stringLen = len(string)
rule = stringLen>=1 and stringLen <= 1000 and stringLen <=20
if(rule):
    print("OK")
else:
    print("NG")
