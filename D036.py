string = str(input())

rule= len(string) >= 1 and len(string) <= 100

if(rule):
    print(string.replace("at","@"))