#すごろくのサイコロ
loop = int(input())
result = 0
rule = loop>= 1 and loop<=100
if(rule):
    n = input().split()
    if(len(n) == loop):
        for _ in n:
            _ = int(_)
            result += _
    print(result)