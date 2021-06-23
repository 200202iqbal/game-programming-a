string = str(input())
rule = len(string) >=1 and len(string) <=20
rule2 = string.find("noaki")
if(rule):
    if "noaki" in string:
        print(string.replace("noaki",""))
    else:
        print(string)