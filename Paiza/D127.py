#座席番号のくじ
lotre = input()
code = lotre[0].upper()
rule = len(lotre) == 4 and type(code) == str
if(rule):
    if(int(lotre[1]) == int(lotre[2]) == int(lotre[3])):
        print("Yes")
    else:
        print("No")