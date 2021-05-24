number = int(input())
string = str(input())
count = 0
countS = 0
countR = 0
rule = number>=1 and number<=100 and len(string) == number
if(rule):
    for s in string:
        if( s == "S"):
            countS +=1
        else:
            countR +=1
    print(countS,countR)