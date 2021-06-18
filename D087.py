number = int(input())
i = 0
words =""
rule = number >=1 and number<=10
if(rule):
    while i<number:
        word = input()
        words += word
        i+=1    
print(words)