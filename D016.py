string = str(input())
number = int(input())
stringLen = len(string)
rule = stringLen,number>=1 and stringLen <=100 and number <= stringLen
if(rule):
    print(string[:number])
