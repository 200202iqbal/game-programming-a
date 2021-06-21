number = int(input())
words = input()
rule = number>=1 and number<=100 and len(words) >=1 and len(words) <=100

if(rule):
    x =words[:number]
    x = str(x)
    print(x)
    