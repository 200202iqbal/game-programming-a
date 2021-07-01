#略語の生成
n = int(input())
words = input().split()
rule = n>=1 and n<=100 and len(words) == n 
newword = "";
if(rule):
    for _ in words:
        newword += _[0]
    print(newword)