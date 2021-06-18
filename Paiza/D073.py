#string reverse
s = str(input())
rule = len(s) >= 1 and len(s) <= 100
if(rule):
    print(s[::-1])