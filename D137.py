string = input()
stringLen = len(string)
rule = stringLen == 10
if(rule):
    hitung = 0
    for y in string:
        if(y == "y"):
            hitung+=1
        
    print(hitung)