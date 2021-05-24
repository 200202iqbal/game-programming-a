string = str(input())
stringLen = len(string)
string = string.lower()
rule = stringLen>=3 and stringLen<=20
if(rule):
    print(string[:3])