string = str(input())
word = str(input())

rule = len(string) >= 2 and len(string)<=100 and len(word) == 1
if(rule):
    
    print(word+string+word)