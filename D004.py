counter = int(input())
loop = 0
word = ""
rule = counter >=1 and counter <=20
if(rule):
    while(loop < counter):
        words = input()
        word = word + words+","
        loop += 1


print("Hello",word[:-1],end=".")