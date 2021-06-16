string = input()
rule = len(string) >=1 and len(string)<=100
if(rule):
    count = 0
    for s in string:
        if(s == "A"):
            count +=1
    print(count)
        