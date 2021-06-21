string = str(input())
rule = len(string) >=1 and len(string) <= 20

if(rule):
    if(len(string)>= 10):
        string1= string[0:10]
        string2 = string[10:]
        print(string1)
        print(string2)
    else:
        print(string)